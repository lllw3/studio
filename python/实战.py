# -*- coding: utf-8 -*-
"""
Created on Sun May 17 16:37:04 2020

@author: Lenovo
"""
import re
import random
import requests
import time
from wget import download
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
#for i in range(2838,3000):
#    txt = requests.get(url.format(i),headers=header).text
#    print(i,len(txt))
#    open('f:\htmls\{}.html'.format(i),'w',encoding='utf-8').write(txt)
#    time.sleep(2)
allhtml=''.join([open('f:\htmls\{}.html'.format(i),'r',encoding='utf-8').read()for i in range(2501,3341)])
len(allhtml)
img_urls=re.findall('data-original="(.*?)"',allhtml,re.S)
f=open('f:\img_urls.txt','a',encoding='utf-8')
[f.write(i+'\n') for i in img_urls]
f.close()
#    ''.json
#allhtml=''.join[open('htmls/{}.html'.format(i),'r',encoding='utf-8').read() i in range (1,20)]
#len(allhtml)
#re.findall=(data-original="(.*?)",allhtml,re.S)
#img_urls=re.findall('data-original="(.*?)"',allhtml,re.S)
#f=open('img_urls.txt','w',encoding='utf-8')
#[f.write(i+'\n')for i in img_urls]
#f.close()
#from wget import download
#open('img_urls.txt','r',encoding='utf-8').readlines()
#[download(i,'imgs4/{}').format(i.split('/')[-1])for i in img_urls[0:1]]
    
    