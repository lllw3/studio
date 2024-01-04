#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 22:40:37 2020

@author: linhaohong
"""

import urllib.request as r
from wget import download
f=open('urls.txt','r',encoding='utf-8')
a=f.readlines()
for i in a:
    print(i.replace('\n','').split('?')[0].split('/')[-1])
    download(i,i.replace('\n','').split('?')[0].split('/')[-1])
    