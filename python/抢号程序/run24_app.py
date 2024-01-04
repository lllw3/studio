from log_tools import log
import urllib3
import requests
import random
import time
import json
from multiprocessing import Process
from settings import *
from net_tools import req,get_order_url,get_last_date
from redis import StrictRedis
from net_tools import *
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def run24(doctorNo,deptCode):
    r = StrictRedis(host='127.0.0.1',port=6379,decode_responses=True)
    while True:#排班
        try:
            start = time.time()#耗时0.58s 
            docData = req(SEARCHDOCTOR_URL)
            _temp=[i['doctor_no'] for i in docData['docArr'] if int(i['dept_code']) == deptCode and int(i['schulde_flag'])==1 ]
            if len(_temp) == 0:
                raise Exception('run24:不可预约')
            log('run24:1.可预约{}'.format(doctorNo))

            last_date = get_last_date(days=7)
            paihaoData=req(CHOOSEDATEEXT_URL.format(doctorNo=doctorNo,deptCode=deptCode),timeout=6)
            # if last_date not in str(paihaoData):
            #     raise Exception('run24:暂未开放余号查询')
            #outpDate,currentWeek,doctorNo,deptCode,timeInterval,scheduleId
            choosedateext_list = [
                (i['mornings'][0]['scheduleInfo']['outpDate'],
                i['mornings'][0]['scheduleInfo']['week'],
                i['mornings'][0]['scheduleInfo']['doctorNo'],
                i['mornings'][0]['scheduleInfo']['deptCode'], 
                i['mornings'][0]['scheduleInfo']['timeInterval'],
                i['mornings'][0]['scheduleInfo']['scheduleId']) 
                for i in 
                    list(paihaoData['scheduleMap'].values()) 
                if len(i['mornings'])>0 and last_date in i['mornings'][0]['scheduleInfo']['outpDate'] and  i['mornings'][0]['scheduleInfo']['reserveNum']>0]
            
            log('run24:1.获取排班日期耗时：{}'.format(time.time()-start))
            break
        except Exception as err:
            log(err.args)
    for outpDate,currentWeek,doctorNo,deptCode,timeInterval,scheduleId in choosedateext_list:    
        while True:#余号
            try:
                log('{} {} {} {} {} {}'.format(outpDate,currentWeek,doctorNo,deptCode,timeInterval,scheduleId))  
                start = time.time()#耗时0.58s 
                yuhaoData = req(SCHEDULETIME_URL.format(scheduleId),timeout=6)
                schedulelist = [ 
                    (get_order_url(ptimeinterval='{} - {}'.format(i['startTime'],i['endTime']),
                                registerDate=outpDate,
                                scheduleId=i['scheduleId'],
                                PartTimeId=i['partTimeId'],
                                deptCode=deptCode,doctorNo=doctorNo,patientId='',
                                autcode='my_autcode',timeInterval=timeInterval),
                                '{} {} - {}'.format(outpDate,i['startTime'],i['endTime']),
                                int(i['remaining_num'])) for i in yuhaoData['schedulelist'] if int(i['remaining_num'])>=0 ]
                #######生成order
                countOrder = sum([i[-1] for i in schedulelist])
                schedulelist = sorted(schedulelist,key=lambda i:i[-1],reverse=True)
                log('run24:2.获取余号{} {} 有余号{}张，耗时：{}'.format(outpDate,currentWeek,countOrder,time.time()-start))
                runOrder(schedulelist)
                break
            except Exception as err:
                #服务器崩溃，或者是连接服务器超时
                log('run24:2.获取医生排班时间异常 {}'.format(err.args))