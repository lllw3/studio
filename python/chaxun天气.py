# -*- coding: utf-8 -*-
"""
Created on Fri May  8 10:20:22 2020

@author: Lenovo
"""


import urllib.request as r
print('请输入要查询的城市（拼音）：')
city=input()
url='http://api.openweathermap.org/data/2.5/weather?q='+city+'&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
data=r.urlopen(url).read().decode('utf-8')

import json
data=json.loads(data)

print(city+'今天天气状况如下')
print('温度是'+str(data['main']['temp'])+'度')
print('天气情况是'+str(data['weather'][0]['description']))