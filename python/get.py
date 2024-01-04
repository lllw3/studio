# -*- coding: utf-8 -*-
"""
Created on Thu May  7 15:35:59 2020

@author: Lenovo
"""


import urllib.request as r
url='http://api.openweathermap.org/data/2.5/weather?q=yancheng&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
data=r.urlopen(url).read().decode('utf-8')

import json
data=json.loads(data)
print('今天广州的天气如下')
print('温度是'+str(data['main']['temp'])+'度')
print('天气情况是'+str(data['weather'][0]['description']))
print('气压是'+str(data['main']['pressure'])+'hPa')
input()

