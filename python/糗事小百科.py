# -*- coding: utf-8 -*-
"""
Created on Sat May 16 12:59:03 2020

@author: Lenovo
"""

import urllib.request as r
import re
from lxml.html import etree
print("shuruyema:")
page=input()
for i in range(int(page)):
    header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'}
    url='https://www.qiushibaike.com/text/page/{}/'.format(page)
    response=r.Request(url,headers=header)
    data=r.urlopen(response).read().decode('utf-8')
    data2=etree.HTML(data)
    data2=data2.xpath('//div[@class="content"]/span/text()')
    l=[]
    for j in data2:
        if j=='查看全文':
            continue
        data3=re.findall('\n*(.*?)\n*',j)
        for x in data3:
            l.append(x)
        if len(re.findall('\n',j))==2:
            l.append('\n')
            l.append('\n')
    with open('f://baike.txt','a',encoding='utf-8') as f:
        for j in l:
            f.write(j)
    print('1yexiazaiwangchen')
         
#headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}