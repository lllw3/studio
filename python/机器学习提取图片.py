# -*- coding: utf-8 -*-
"""
Created on Sun May 31 10:06:50 2020

@author: Lenovo
"""


from selenium.webdriver import Chrome
import urllib.request as r
import time
def openUrl():
    web = Chrome(executable_path ='chromedriver.exe')
    # web.grt('http://www.baidu.com')
    # ele = web.find_element_by_path("//*[@class='s_ipt']")
    # ele
    #打开网页
    url='http://ics.autohome.com.cn/passport/'
    web.get(url)
    return web
web = openUrl()
def getImgUrl(web):
    #查找元素
    #ele = web.find_element_by_xpath("//*[@class='geetest_radar_tip_content']")
    #元素操作（点击元素）、可能不起作用执行js控制
    #ele.click()
    #执行javascript代码
    #web.execute_script("document.getElementsByClassName('geetest_radar_tip')[0].click()")
    time.sleep(2)
    web.execute_script("document.getElementsByClassName('geetest_radar_tip_content')[0].click()")
    #获取图片地址
    ele = web.find_element_by_xpath('//*[@class="geetest_item_img"]')
    #ele 
    #获取图片元素
    #img_url = ele.get_attribute('src')
    #截断地址
    #img_url = img_url.split('?')[0]
    img_url = ele.get_attribute('src').split('?')[0]
    #img_url 
    #下载图片
    r.urlretrieve(img_url,'imgs/'+img_url.split('/')[-1])
    while True:
        try:
            web.execute_script("document.getElementsByClassName('geetest_refresh')[0].click()")
            time.sleep(2)
            ele = web.find_element_by_xpath("//*[@class='geetest_item_img']")
            img_url = ele.get_attribute('src').split('?')[0]
            print(img_url)
            r.urlretrieve(img_url,'imgs/'+img_url.split('/')[-1])
        except Exception as err:
            print(err.args)
            break;
getImgUrl(web)
            

