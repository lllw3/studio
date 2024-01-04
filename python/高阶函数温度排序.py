# -*- coding: utf-8 -*-
"""
Created on Tue May 12 16:02:29 2020

@author: Lenovo
"""



import urllib.request as r
url='http://api.openweathermap.org/data/2.5/forecast?q=guangzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')

import json
temp=[]
data=json.loads(data)
for i in range(len(data['list'])):
    temp.append(data['list'][i]['main']['temp'])
temp_s=sorted(temp)
temp_s.sort(reverse=True)
print('从小到大')
print(temp_s)
print('从大到小')
print(temp)
#高阶函数温度排序
print('按绝对值大小排序')
s=sorted(temp,key=abs)
print(s)
print('反向排序')
t=sorted(temp,key=abs,reverse=True)
print(t)
