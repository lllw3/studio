# -*- coding: utf-8 -*-
"""
Created on Mon May 11 17:08:28 2020

@author: Lenovo
"""


# -*- coding: utf-8 -*-
"""
Created on Fri May  8 08:55:04 2020

@author: Lenovo
"""


#实现动态城市输入全球天气查询
#导入拼音库
from pypinyin import lazy_pinyin
#自定义函数中文转化拼音
def get_pinyin(word):
    result=lazy_pinyin(word)  #转换为拼音
    result=''.join(result)  #把每个汉字的拼音连接起来
    return result
def save(data):
    with open("weatherdata.txt",'w',encoding = 'utf-8') as fp:
        fp.write(data)
    return True
def read():
    with open("weatherdata.txt",'r',encoding = 'utf-8') as fp:
        fp.read()


#导入联网工具包
import urllib.request as r
#用户输入查询
print('请输入要查询的城市：')
city=input()
city_n=get_pinyin(city)  #转换为拼音
url1='http://api.openweathermap.org/data/2.5/weather?q='+city_n+'&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
url2='http://api.openweathermap.org/data/2.5/forecast?q='+city_n+',cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data1=r.urlopen(url1).read().decode('utf-8')
data2=r.urlopen(url2).read().decode('utf-8')

#转换格式
import json
data1=json.loads(data1)  #当前天气数据
data2=json.loads(data2)  #未来天气数据
#输出当前天气状况
print(city+'今天天气状况如下')
print('温度是'+str(data1['main']['temp'])+'度')
print('天气情况是'+str(data1['weather'][0]['description']))
i=2
data=[]
print('==========未来五天天气状况如下===========')
while i <39:
    a1=str(data2['list'][i]['dt_txt']))
    a2=str(data2['list'][i]['main']['temp']))
    a3=str(data2['list'][i]['main']['pressure']))
    a4=str(data2['list'][i]['weather'][0]['description']))
    print('温度折线图是'+'--' * int(data2['list'][i]['main']['temp']))
    print('*'*80)  #用*分割排版输出界面
    data.append(a1)
    data.append(a2)
    data.append(a3)
    data.append(a4)
    i +=8
f=open('test.txt',encoding='utf-8')   #打开文件
data=f.read()            #文件操作
print(data)
f.close()  



   


#温度折线图
#import matplotlib.pyplot as plt
#from matplotlib.font_manager import FontProperties
#font=FontProperties(fname=r"c:\windows\fonts\simsun.ttc",size=15)
#Temp=[data1['main']['temp']]
#for j in range(5):
 #   Temp.append(data2['list'][j]['main']['temp'])
#plt.plot(Temp,label='温度')
#plt.legend(loc=2)
#plt.xlabel('日期',fontproperties=font)
#plt.ylabel('温度（摄氏度）',fontproperties=font)
#plt.title('近五日天气温度变化图',fontproperties=font)
#plt.xlim((0,5))

