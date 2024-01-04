from settings import *
from log_tools import log
import schedule
from multiprocessing import Process
import time
from run2min_app import run2min
from run24_app import run24
from cookies_app import updateCookies
def main():
    '''抢号入口'''
    for i in [(DOCTORNO_212820,DEPTCODE_212820,),(DOCTORNO_70,DEPTCODE_70,)]:
        p = Process(target=run24,args=i)
        p.start()#开始进程
    ###更新cookies
    Process(target=updateCookies).start()#开始进程
    #run2min任务
    schedule.every().monday.at('20:00').do(run2min,DOCTORNO_212820,DEPTCODE_212820)#周一
    schedule.every().tuesday.at('20:00').do(run2min,DOCTORNO_212820,DEPTCODE_212820)#周二
    schedule.every().wednesday.at('20:00').do(run2min,DOCTORNO_212820,DEPTCODE_212820)#周三
    schedule.every().sunday.at('20:00').do(run2min,DOCTORNO_70,DEPTCODE_70)#周日
    while True:
        schedule.run_pending()
        time.sleep(1)
    log('所有程序已经正常运行')

if __name__=='__main__':
    main()

