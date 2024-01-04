# -*- coding: utf-8 -*-
"""
Created on Sun May 17 17:34:47 2020

@author: Lenovo
"""


#import random
#import requests
#import time
#from wget import download
#import re
import urllib
import urllib.request
#url='https://www.doutula.com/photo/list/?page={}'
#my_headers = [
#        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
#        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
#        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
#        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
#        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
#        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
#        ]
#header = {"User-Agent": random.choice(my_headers)}
#for i in range(2340,2501):
#    txt = requests.get(url.format(i),headers=header).text
#    print(i,len(txt))
#    open('f:\htmls\{}.html'.format(i),'w',encoding='utf-8').write(txt)
#    time.sleep(3)

#allhtml=''.join([open('f:\htmls\{}.html'.format(i),'r',encoding='utf-8').read()for i in range(20,3341)])
#len(allhtml)
#img_urls=re.findall('data-original="(.*?)"',allhtml,re.S)
#f=open('f:\img_urls.txt','a',encoding='utf-8')
#[f.write(i+'\n') for i in img_urls]
#f.close()
img_urls=open('f:\img2.txt','r',encoding='utf-8').readlines()
#[download(i,'f:\imgs\{}'.format(i.split('/')[-1])) for i in img_urls]
x=1
for urla in img_urls:
    try:
        urllib.request.urlretrieve(urla, 'f:\imgs\%s.gif' % x)
        x=x+1
        print('1')
    except:
        pass