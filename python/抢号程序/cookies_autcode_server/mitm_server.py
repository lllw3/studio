from mitmproxy import http
from json import dumps,loads
from redis import StrictRedis
import requests
from multiprocessing import Process
import time
print('--111---->')
from my_web import get_autcode  
#服务器的地址，端口
r = StrictRedis(host='127.0.0.1',port=6379,decode_responses=True)#decode_responses=True 返回数据都是字符串

def request(flow: http.HTTPFlow):##autcode=D1FC39F922FB45C7A61DFE3015BE46BE
    print('--1---->',flow.request.url)
    if '&autcode=' in flow.request.url and 'cardNumber' in flow.request.url and '&q666=q666' not in flow.request.url:
        autcode = flow.request.url.split('&autcode=')[1].split('&')[0]
#         cardNumber = flow.request.url.split('&cardNumber=')[1].split('&')[0]
        # print(cardNumber,autcode,msg[cardNumber])
        if 'Cookie'in flow.request.headers.keys() and 'https://dyh.xqyy.com.cn' in flow.request.url:
            JSESSION = flow.request.headers["Cookie"].split('JSESSIONID=')[-1].replace('; 0=','').replace('; 0','')
        name = r.hget('session_name',JSESSION)
        r.hset('names',name,JSESSION+'-'+autcode)
        print('插入autcodes成功',autcode,JSESSION)
        flow.kill()

def response(flow: http.HTTPFlow): 
    print('=1====>',flow.request.url)
    JSESSION = ''
    if 'Cookie'in flow.request.headers.keys() and 'https://dyh.xqyy.com.cn' in flow.request.url:
        JSESSION = flow.request.headers["Cookie"].split('JSESSIONID=')[-1].replace('; 0=','').replace('; 0','')
    if len(JSESSION)<=10:
        return
    if 'electornichealthcard?cls=ehc&m=getDynamicQRCode&patientId=' in flow.request.url: 
        name = loads(flow.response.text)['healthcard']['name']
        print('qqyu====',name)
        session_code = r.hget('names',name)
        if session_code == None:
            session_code = '-'
        
        r.hset('names',name,JSESSION + '-' + session_code.split('-')[1])   
        r.hset('session_name',JSESSION,name)  
    if 'https://dyh.xqyy.com.cn/center?cls=pc&m=getUserInfo&funcId=function02'==flow.request.url:
        p = Process(target=get_autcode,args=(JSESSION,))
        p.start()#开始进程