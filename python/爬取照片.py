# -*- coding: utf-8 -*-
"""
Created on Sat May  9 18:17:10 2020

@author: Lenovo
"""

import requests
from lxml import etree
import re

#文本信息保存在test.txt
file = open("test.txt",'w',encoding='utf-8')

url = "http://www.pythonscraping.com/pages/page3.html"

res = requests.get(url)
content = res.content
html = etree.HTML(content)

#数据解析
title = html.xpath('//*[@class="gift"]/td[1]/text()')
desc =  html.xpath('//*[@class="gift"]/td[2]')
price = html.xpath('//*[@class="gift"]/td[3]/text()')
imgs=html.xpath('//*[@class="gift"]/td[4]/img/@src')

#写入文件
x = len(title)
for i in range(0,x):
    descText = desc[i].xpath('string(.)')

    file.write("第"+str(i+1)+"行数据"+"\n"+title[i]+"\n"+descText+"\n"+price[i]+"\n\n")

    with open('D:/image'+str(i)+'.jpg', 'wb') as fd:
        picture=requests.get('http://www.pythonscraping.com/x/'+imgs[i]).content
        fd.write(picture)
        print("成功下载%s.jpg"%i)

#关闭文件
file.close()


