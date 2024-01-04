# -*- coding: utf-8 -*-
"""
Created on Sun May 17 11:40:50 2020

@author: Lenovo
"""


import requests



#https://www.doutula.com/photo/list/ 
#//*[@id="pic-detail"]/div/div[2]/div[2]/ul/li/div/div/a[1]/img
#//*[@id="pic-detail"]/div/div[2]/div[2]/ul/li/div/div/a[2]/img
#//*[@id="pic-detail"]/div/div[2]/div[2]/ul/li/div/div/a[3]/img
        #。。。
#//*[@id="pic-detail"]/div/div[2]/div[2]/ul/li/div/div/a[68]/img
        
        
#https://www.doutula.com/photo/list/?page=2       
#//*[@id="pic-detail"]/div/div[2]/div[2]/ul/li/div/div/a[1]/img
#//*[@id="pic-detail"]/div/div[2]/div[2]/ul/li/div/div/a[68]/img

import random
#第一页
def get_one():
    url='https://www.doutula.com/photo/list/'
    my_headers = [
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        ]
    header = {"User-Agent": random.choice(my_headers)}
    html_str = requests.get(url,headers=header).text
    with open('f:\doutuladata1.txt','w',encoding='utf-8') as f:  
        f.write(html_str)
#第n页
from lxml import etree
from lxml.etree import HTML
url='https://www.doutula.com/photo/list/?page={}'
my_headers = [
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        ]
header = {"User-Agent": random.choice(my_headers)}
url_list=[]
for i in range(1,333):
    url_list.append(url.format(i))
for page in url_list:
    html_str = requests.get(page,headers=header).text
    with open('f:\doutuladata2.txt','a',encoding='utf-8') as f:  
        f.write(html_str)
        print('保存完成')
html = etree.HTML(html_str)
img_xpath='//*[@id="pic-detail"]/div/div[2]/div[2]/ul/li/div/div/a[.]/img/@data-original'
img_html = html.xpath(img_xpath)
open('img','wb').write(img_html)
img_name_xpath='//*[@id="pic-detail"]/div/div[2]/div[2]/ul/li/div/div/a[1]/img'
img_list=html.xpath(img_name_xpath)
open('img3','wb').write(img_list)
#selector=HTML(text=html_str)

#img_ls=[]
#img_ls.append(selector.xpath(img_xpath))
#for i in range(1,30):
#    with open('f:\斗图采集集合\img_path'+str(i)+'.jpg', 'wb') as fd:
#        picture=requests.get('https://www.doutula.com/photo/list/'+img_ls[i]).content
#        fd.write(picture)
#        print("成功下载%s.jpg"%i)