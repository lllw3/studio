import requests
import random
import time
from datetime import timedelta
from datetime import datetime
from redis import StrictRedis
from log_tools import log
import grequests
from settings import *
import pyautogui
r = StrictRedis(host='127.0.0.1',port=6379,decode_responses=True)#decode_responses=True 返回数据都是字符串

def req(url,cookies='',timeout=10):
    if cookies=='':
        # if i.split('-')[1]!=''
        cookies_autcode_ls = [(i.split('-')[0],i.split('-')[1]) for i in list(r.hgetall('names').values())]
        if len(cookies_autcode_ls)==0:
            time.sleep(3)
            raise Exception('缺少验证码信息')
        cookies = random.choice(cookies_autcode_ls)[0]

    resp = requests.get(url,cookies={'JSESSIONID':cookies},timeout=timeout,verify=False).json()
    if int(resp['rc']) == -1:
        if resp['msg']=='搜索医生异常':#cookies失效
            time.sleep(2)
            log('cookies失效，触发点击个人中心页面')
        raise Exception(resp['msg'])
    return resp

def get_order_url(ptimeinterval='08:30 - 09:00',registerDate='2020-07-27',scheduleId='90711a076e264a269d2da7a80de709fb',PartTimeId='1f5af481affa49e2ae01c467b53908f4',deptCode='70',doctorNo='935124d6fc5e47708661c98d007cc075',patientId='04522103-e6b1-4731-85a7-f75164d9afca',autcode='',timeInterval='AM'):
    params={
        'cls':'yygh','m': 'doOrder',0: {"undertaker":""},1: {"paymore":""},
        10: {"registerDate":""},11: {"registerfee":""},12: {"registrationfee":""},13: {"clinicfee":""},
        14: {"defaulttype":""},15: {"ptimeinterval":""},16: {"doctor_title":""},17: {"patientId":""},
        18: {"payMode":""},19: {"cardNumber":""},2: {"visitCode":"0"},20: {"paymoney":""},21: {"querycode":""},
        3: {"accountId":""},4: {"doctorNo":""},5: {"deptCode":""},6: {"outptyp":""},7: {"scheduleId":""},
        8: {"timeInterval":""},9: {"PartTimeId":""},
        'undertaker': 0,'visitCode': 0,'clinicfee': 0,'defaulttype': 1,'doctorNumType': '',
        'doctor_title': '','funcId': 'function03','isCancelLock': 0,'payMode': 1,
        'paymoney': '500.0','paymore': '0.0','registerfee': '5000.0','registrationfee': '5000',
        'ptimeinterval': ptimeinterval,#1
        'registerDate': registerDate,#2
        'scheduleId': '90711a076e264a269d2da7a80de709fb',#3
        'PartTimeId': '1f5af481affa49e2ae01c467b53908f4',#4
        'cardNumber': '130984198901153912',#5
        'deptCode': '70',##6
        'doctorNo': '935124d6fc5e47708661c98d007cc075',#7
        'patientId': '04522103-e6b1-4731-85a7-f75164d9afca',#8
        'autcode': '',#9
        'timeInterval': 'AM'#10
    #     'startTime': '08:30',
    #     'endTime': '09:00',
    }
    params['ptimeinterval']=ptimeinterval#1
    params['registerDate']=registerDate#2
    params['scheduleId']=scheduleId#3
    params['PartTimeId']=PartTimeId#4
    params['cardNumber']='51292119490929097X'#5
    params['deptCode']=deptCode#6
    params['doctorNo']=doctorNo#7
    params['patientId']=patientId#8
    params['autcode']=autcode#9
    params['timeInterval']=timeInterval#10
    url='https://dyh.xqyy.com.cn/reservegh?'
    for key in params:
        url=url+'{}={}&'.format(key,params[key])
    return url[0:-1]+'&q666=q666'

def get_last_date(days=8):
    now = datetime.now()
    delta = timedelta(days=days) 
    n_days_after = now + delta  #当前日期推迟n天之后的时间
    return n_days_after.strftime('%Y-%m-%d')

def callback(respon, *args, **kwargs):#更新验证码
    print('callback....',respon.url)
    autcode = respon.url.split('autcode=')[1].split('&')[0]
    names = r.hgetall('names')
    for name in names:
        if autcode in names[name]:
            r.hset('names',name,names[name].replace(autcode,''))
            break
    print('抢号完毕',respon.json()['msg'])

def exception_handler(respon, exception):#更新验证码
    print('exception_handler...')
    autcode = respon.url.split('autcode=')[1].split('&')[0]
    names = r.hgetall('names')
    for name in names:
        if autcode in names[name]:
            r.hset('names',name,names[name].replace(autcode,''))
            log('抢号失败:{},{}'.format(name,exception.args))
            break
    print('抢号err')

def runOrder(schedulelist):
    tasks = []
    cookies_autcode_ls = [(i.split('-')[0],i.split('-')[1]) for i in list(r.hgetall('names').values()) if i.split('-')[1]!='']
    if len(cookies_autcode_ls)==0:
        raise Exception('runOrder:缺少验证码信息')

    for cookies,autcode in cookies_autcode_ls:
        order_url = random.choice(schedulelist)[0].replace('my_autcode',autcode)
        task = grequests.get(order_url,cookies={'JSESSIONID':cookies},callback=callback,verify=False)
        tasks.append(task)
    
    grequests.map(tasks, exception_handler=exception_handler, gtimeout=12)
