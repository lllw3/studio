# -*- coding: utf-8 -*-
"""
Created on Wed May 20 09:24:28 2020

@author: Spirit H
"""


import requests
import re

def get_websitdata():
    url = 'https://jobs.51job.com/xian/122218533.html'#.format(index)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}
    response = requests.get(url , headers = headers)

    response.encoding = 'utf-8'
    data = response.content.decode('gbk')

    return data

def get_label(data):
    label = re.findall('<span class="sp4">(.*?)</span>' , data)
    return label#list
    
data = get_websitdata()
l = get_label(data)
print(l)
#print(data)
