from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import json
import time
import os
from datetime import date
from datetime import datetime
from datetime import timedelta
import random
from opencv_ai import open_cv
import requests

def getWeb(piaoUrl,cookies):
    '''配置web浏览器'''
    options = webdriver.ChromeOptions()
    mobile_emulation = {"deviceName": "Galaxy S5"}
    capabilities = DesiredCapabilities.CHROME
    capabilities['loggingPrefs'] = {'browser': 'ALL'}
    # options = webdriver.ChromeOptions()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    # 修改windows.navigator.webdriver，防机器人识别机制，selenium自动登陆判别机制desired_capabilities=capabilities,
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # 更换头部
    options.add_argument('user-agent=mozilla/5.0 (iphone; cpu iphone os 5_1_1 like mac os x) applewebkit/534.46 (khtml, like gecko) mobile/9b206 micromessenger/5.0')
    #禁用图片
    #禁止图片和css加载
    prefs = {'permissions.default.stylesheet':2}#"profile.managed_default_content_settings.images": 2,
    options.add_experimental_option("prefs", prefs)
    #添加代理
    ip,port = '127.0.0.1','8080'
    options.add_argument(('--proxy-server=http://{}:{}'.format(ip,port)))#有的博客写的是'--proxy-server=http://'，就目前我的电脑来看的话需要把http://去掉就可以用，他会自己加的
    # options.add_argument('-headless')  # 无头参数
    # options.headless = True
    web = webdriver.Chrome(executable_path='./chromedriver.exe',options=options)
    url = "https://61.186.173.202/"
    web.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined
        })
    """
    })
    web.set_page_load_timeout(30)
    web.set_script_timeout(30)#这两种设置都进行才有效
    web.get(piaoUrl)
    web.add_cookie({'name': 'JSESSIONID','path': '/','value': cookies})
    return web

def slide(tracks,web):
    '''根据pointX进行滑动'''
    slider = web.find_element_by_xpath('//*[@id="captcha"]/div/div[2]/div')
    # slider = self.driver.find_element_by_xpath(‘//*[@id="captcha"]/div/div[3]/div[2]‘)
    # 鼠标点击并按住不松
    webdriver.ActionChains(web).click_and_hold(slider).perform()
    # 让鼠标随机往下移动一段距离
    ActionChains(web).move_by_offset(xoffset=0, yoffset=100).perform()
    time.sleep(0.15)
#     for item in tracks:
#         ActionChains(web).move_by_offset(xoffset=item, yoffset=random.randint(-2,2)).perform()
    ActionChains(web).move_by_offset(xoffset=tracks[0], yoffset=random.randint(-2,2)).perform()
    # 稳定一秒再松开
    time.sleep(0.5)
    ActionChains(web).release(slider).perform()
    time.sleep(1)
    # 随机拿开鼠标
    ActionChains(web).move_by_offset(xoffset=random.randint(200, 300), yoffset=random.randint(200, 300)).perform()
    #检测是否滑动验证码成功
    WebDriverWait(web, 8).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="loading"]/div')))

def qiangpiao(web):
    #打开抢票界面
    ############wait
    xpath='//*[@id="register-info"]/div[3]/div/div[2]'
    WebDriverWait(web, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    ## 触发打开抢票界面验证码
    web.execute_script("document.getElementsByClassName('sure color_background')[0].click()")
    while True:
        try:
            # xpath='//*[@id="register-info"]/div[3]/div/div[2]'
            # WebDriverWait(web, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            # ## 触发打开抢票界面验证码
            # web.execute_script("document.getElementsByClassName('sure color_background')[0].click()")
            ############wait
            img = WebDriverWait(web, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="captcha"]')))
            # 触发打开抢票界面验证码-开始截屏
            time.sleep(1)
            ele=web.find_element_by_xpath('//*[@id="captcha"]/canvas[1]')
            picId = web.session_id
            ele.screenshot('cookies_autcode_server/output/captcha{}.png'.format(picId))
            slide(open_cv(picId),web)
            time.sleep(1)
            if "加载" in web.find_element_by_xpath('//*[@id="loading"]/div').text:
                return True
        except:
            pass

def get_autcode(cookies,ok_url='https://dyh.xqyy.com.cn/#/register-info?registerfee=50.0&outpdate=2020-08-02&scheduleid=636ddf5787664a11ab5abdc6eece9bdb&timeinterval=AM&currWeek=周二&registrationfee=0&clinicfee=50&doctor_title=主任医师&deptCode=212820&doctorNo=2baf47ce661741e2b54a2bde72051411&PartTimeId=c78418e0343b45d98f9d235e7f58dee3&outptypename=中医科专家号晋&doctorNumType=中医科专家号晋&startTime=09:30&endTime=10:00'):
    while True:
        try:
            print('启动浏览器',cookies)
            web = getWeb(ok_url,cookies)
            ###等待是否启动
            time.sleep(3)
            if '晋献春' not in web.page_source:
                continue  
            if qiangpiao(web):
                web.quit()
                print('获取autcode成功')
                break
        except Exception as err:
            print(err.args,'滑动验证码错误')
        try:
            web.quit()
        except Exception as err:
            pass
    
# if __name__=='__main__':
#     getWeb()