from net_tools import req
import pyautogui
from settings import *
from redis import StrictRedis
import time
from log_tools import log

#服务器的地址，端口
r = StrictRedis(host='127.0.0.1',port=6379,decode_responses=True)#decode_responses=True 返回数据都是字符串

def updateCookies():
    print('启动cookies监听进程...')
    while True:
        cookies_autcode_dict = r.hgetall('names')
        for name in cookies_autcode_dict:
            i = cookies_autcode_dict[name]
            cookies,autcode = i.split('-')[0],i.split('-')[1]
            errMsg = ''
            try:
                req(SEARCHDOCTOR_URL,cookies=cookies)
            except Exception as err:
                errMsg = str(err.args).lower()
            if 'timeout' in errMsg:
                time.sleep(60)
            elif '搜索医生异常' in errMsg or autcode=='':#cookies失效
                pyautogui.click(POSITIONS[name])
                log('开始更新{} 的cookies以及验证码'.format(name))
                time.sleep(25)
            
        time.sleep(5)