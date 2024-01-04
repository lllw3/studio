from net_tools import req
import pyautogui
from settings import *
from redis import StrictRedis
import time
from log_tools import log

#服务器的地址，端口
r = StrictRedis(host='127.0.0.1',port=6379,decode_responses=True)#decode_responses=True 返回数据都是字符串

def updateCookies():
    while True:
        try:
            cookies_autcode_dict = r.hgetall('names')
            for name in cookies_autcode_dict:
                i = cookies_autcode_dict[name]
                cookies,autcode = i.split('-')[0],i.split('-')[1]
                docData = req(SEARCHDOCTOR_URL,cookies=cookies)
                if docData['msg']=='搜索医生异常' or autcode=='':#cookies失效
                    pyautogui.click(POSITIONS[name])
                    log('开始更新{} 的cookies以及验证码'.format(name))
        except Exception as err:
            if 'timeout' in str(err.args).lower():
                time.sleep(60)
        time.sleep(1)