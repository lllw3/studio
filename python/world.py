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

#保存json数据
filename='data.json'
#with open(filename,'w') as file_obj:
#     json.dump(data2,file_obj)
#输出当前天气状况
print(city+'今天天气状况如下')
print('温度是'+str(data1['main']['temp'])+'度')
print('天气情况是'+str(data1['weather'][0]['description']))
#询问用户是否查询未来天气
print('是否要查询当前城市未来五天天气：(yes/no):')
#用户输入
A=input()
Y='yes'
i =2
weather=[]
#判断是否查询
if A==Y:
    print('==========未来五天天气状况如下===========')
    #检索list查找并输出未来五天12:00的相关信息   
    #检索从第二个开始，共有5个，分别是2,10,18,26,34
    while i <39:
        print(str(data2['list'][i]['dt_txt']))
        print('温度是'+str(data2['list'][i]['main']['temp'])+'度')
        #print('气压是'+str(data2['list'][i]['main']['pressure'])+'hPa')
        #print('天气情况是'+str(data2['list'][i]['weather'][0]['description']))
        #print('温度折线图是'+'--' * int(data2['list'][i]['main']['temp']))
        #print('*'*80)  #用*分割排版输出界面
        i +=8
        weather.append(city+str(data2['list'][i]['dt_txt'])+str(data2['list'][i]['main']['temp']))
        with open(filename,'w') as file_obj:
            json.dump(weather,file_obj)  
        with open(filename) as file_obj:
    weather= json.load(file_obj)
    print(weather)
    end=input('输入任意退出')  #结束查询
else:
    print('查询结束')
    end=input('输入任意退出')
with open(filename) as file_obj:
    data = json.load(file_obj)
    print(data)
    


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

