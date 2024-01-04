# -*- coding: utf-8 -*-
"""
Created on Mon May 11 17:00:35 2020

@author: Lenovo
"""


#导入联网工具包
import urllib.request as r
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')

#转换格式
import json
data=json.loads(data)
#输出所查询的城市名 
print('城市是'+str(data['city']['name']))  
temp=[]
i=2
while i<40:
    print('日期是'+str(data['list'][i]['dt_txt']))
    print('温度是'+str(data['list'][i]['main']['temp'])+'度')
    print('情况是'+str(data['list'][i]['weather'][0]['description']))
    temp.append(data['list'][i]['weather'][0]['description'])
    print('气压是'+str(data['list'][i]['main']['pressure'])+'hPa')
    print('最高温度是'+str(data['list'][i]['main']['temp_max'])+'度')
    print('最低温度是'+str(data['list'][i]['main']['temp_min'])+'度')
    print('温度折线图是'+'--' * int(data['list'][i]['main']['temp']))
    #判断天气情况并给出相关tips/建议
    if str(data['list'][i]['weather'][0]['description']) == '晴':
        print('tips:今日天气极好，游玩愉快！')
    if str(data['list'][i]['weather'][0]['description']) == '雨':
        print('tips:有雨，出门请带好伞！')
    #用*排版分割每日信息
    print('*'*30)
    i += 8
temp_sort=sorted(temp)
a=0
while x<40:
    print(str(data['list'][i]['dt_txt'])+' ', end='\r')
    x +=8
while a<37:
    while j<6:
        if int(temp[j])>0:
            print('||'+' '*18,end='\r')
        temp[j]=temp[j]-1
        j=j+1
    a=a+1
            
            
            
            
    