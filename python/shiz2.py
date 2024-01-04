# -*- coding: utf-8 -*-
"""
Created on Mon May 18 09:03:07 2020

@author: Lenovo
"""


import urllib
import urllib.request
img_urls=open('f:\ing3.txt','r',encoding='utf-8').readlines()

x=41755
for urla in img_urls:
    urllib.request.urlretrieve(urla, 'f:\imgs1\%s.gif' % x)
    x=x+1
    print('1')