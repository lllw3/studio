# -*- coding: utf-8 -*-
"""
Created on Mon May 18 09:59:41 2020

@author: Lenovo
"""



import urllib
import urllib.request
img_urls=open('f:\img_urls.txt','r',encoding='utf-8').readlines()

x=50000
for urla in img_urls:
    try:
        urllib.request.urlretrieve(urla, 'f:\img21\%s.gif' % x)
        x=x+1
        print('1')
    except:
        pass