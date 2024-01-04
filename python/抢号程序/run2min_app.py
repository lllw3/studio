from log_tools import log
import urllib3
import requests
import random
import time
import json
from multiprocessing import Process
from settings import *
from net_tools import *
from redis import StrictRedis
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#服务器的地址，端口
r = StrictRedis(host='127.0.0.1',port=6379,decode_responses=True)#decode_responses=True 返回数据都是字符串

def run2min(doctorNo,deptCode):
    log('run2min:成功启动抢号程序')
    while True:#排班
        try:
            start = time.time()#耗时0.58s 
            last_date = get_last_date(days=8)
            paihaoData=req(CHOOSEDATEEXT_URL.format(doctorNo=doctorNo,deptCode=deptCode),timeout=6)
            if last_date not in str(paihaoData):
                raise Exception('run2min:暂未开放余号查询')
            outpDate,currentWeek,doctorNo,deptCode,timeInterval,scheduleId = [
                (i['mornings'][0]['scheduleInfo']['outpDate'],
                i['mornings'][0]['scheduleInfo']['week'],
                i['mornings'][0]['scheduleInfo']['doctorNo'],
                i['mornings'][0]['scheduleInfo']['deptCode'], 
                i['mornings'][0]['scheduleInfo']['timeInterval'],
                i['mornings'][0]['scheduleInfo']['scheduleId']) 
                for i in 
                    list(paihaoData['scheduleMap'].values()) 
                if len(i['mornings'])>0 and last_date in i['mornings'][0]['scheduleInfo']['outpDate'] ][0]
            
            log('run2min:1.获取排班日期耗时：{}'.format(time.time()-start))
            log('{} {} {} {} {} {}'.format(outpDate,currentWeek,doctorNo,deptCode,timeInterval,scheduleId))  
            break
        except Exception as err:
            log('run2min:{}'.format(err.args))

    while True:#余号
        try:
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
            log('2.获取余号{} {} 有余号{}张，耗时：{}'.format(outpDate,currentWeek,countOrder,time.time()-start))
            break
        except Exception as err:
            #服务器崩溃，或者是连接服务器超时
            log('run2min:2.获取医生排班时间异常 {}'.format(err.args))
    
    #启动循环23小时
    for t in range(1380*60):#23*60*60，循环23小时
        if t == 0:
            runOrder(schedulelist)
            time.sleep(30)#等待一分钟再次查询是否可以预约
            continue
        try:
            docData = req(SEARCHDOCTOR_URL.format(deptCode))
            _temp=[i['doctor_no'] for i in docData['docArr'] if int(i['dept_code']) == deptCode and int(i['schulde_flag'])==1 ]
            if len(_temp) == 0:
                raise Exception('不可预约')
            runOrder(schedulelist)
            log('run2min:3.可预约{}'.format(_temp))
        except Exception as err:
            log('run2min:3不可预约{}'.format(err.args))
        time.sleep(60)#等待一分钟再次查询是否可以预约
