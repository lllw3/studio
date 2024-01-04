# -*- coding: utf-8 -*-
"""
Created on Fri May 15 14:28:15 2020

@author: Lenovo
"""
from flask import Flask
app = Flask(__name__)
import requests
#import urllib.request as r
import json
from pypinyin import lazy_pinyin
import re
def get_pinyin(word):
    result=lazy_pinyin(word)  #转换为拼音
    result=''.join(result)  #把每个汉字的拼音连接起来
    return result
@app.route('/')
def weather():
    all_city=['西安','北京','惠州','杭州','北京','广州','重庆','吉林','梅州','深圳','江门','厦门','香港','上海','天津','苏州','武汉','台湾','桂林','南昌']
    all_city_py=[]
    for i in range(len(all_city)):
        all_city_py.append(get_pinyin(all_city[i]))
    city=[]
    for i in all_city_py:
        url='http://api.openweathermap.org/data/2.5/weather?q='+i+'&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
        demo=requests.get(url).text
        t1=re.findall('"temp":(.*?),',demo)[0]
        t2= re.findall('"main":(.*?),',demo)[0]
    #city={'city':i,'temp':t1,'main':t2}
    #print('已获取城市信息：'+str(city))
    #with open('weather30.txt','a',encoding='utf-8') as f:
        city.append(str(i)+t1+t2)
        print('city:'+i+'get')
    city=json.dumps(city)
    return city
            
#print('城市天气信息保存成功')
if __name__ =='__main__':
    app.run()
#host="0.0.0.0",debug=True,port=8888
