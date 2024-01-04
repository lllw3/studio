# -*- coding: utf-8 -*-
"""
Created on Thu May  7 07:55:23 2020
@author: Lenovo
"""
# 求出未来五天天气
# 1.打印每天的12:00的天气（城市，气温，情况，气压，最高温，最低温）
# 2.同上写出英文版
# 3.根据天气的情况，给出建议：例如 今天下雨，提示带伞。今天温度高，穿衬衫...
# 4.根据温度打出打印出问题曲线图 28—————————————————————— 30——————————————...



from pypinyin import lazy_pinyin
#自定义函数中文转化拼音
def get_pinyin(word):
    result=lazy_pinyin(word)  #转换为拼音
    result=''.join(result)  #把每个汉字的拼音连接起来
    return result
#导入联网工具包
import urllib.request as r
print('请输入要查询的城市：')
city=input()
city_n=get_pinyin(city)  #转换为拼音
url1='http://api.openweathermap.org/data/2.5/weather?q='+city_n+'&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
url2='http://api.openweathermap.org/data/2.5/forecast?q='+city_n+',cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data1=r.urlopen(url1).read().decode('utf-8')
data2=r.urlopen(url2).read().decode('utf-8')


#url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
#data=r.urlopen(url).read().decode('utf-8')

#转换格式
import json
data1=json.loads(data1)  #当前天气数据
data2=json.loads(data2)  #未来天气数据
#data=json.loads(data)
print('=='*30)
print(city+'今天天气状况如下')
print('温度是'+str(data1['main']['temp'])+'度')
print('天气情况是'+str(data1['weather'][0]['description']))
print('==========未来五天天气如下==========')
#定义函数求未来五天某个时间的天气
def forecast(i):
    while i<40:
        print('日期是'+str(data2['list'][i]['dt_txt']))
        print('温度是'+str(data2['list'][i]['main']['temp'])+'度')
        print('情况是'+str(data2['list'][i]['weather'][0]['description']))
        print('气压是'+str(data2['list'][i]['main']['pressure'])+'hPa')
        print('最高温度是'+str(data2['list'][i]['main']['temp_max'])+'度')
        print('最低温度是'+str(data2['list'][i]['main']['temp_min'])+'度')
        print('温度折线图是'+'--' * int(data2['list'][i]['main']['temp']))
    #判断天气情况并给出相关tips/建议
        if str(data2['list'][i]['weather'][0]['description']) == '晴':
            print('tips:今日天气正好！')
        if str(data2['list'][i]['weather'][0]['description']) == '雨':
            print('tips:有雨，出门请带好伞！')
        else:
            print('tips:天气不错，出行愉快！')
    #用*排版分割每日信息
        print('=='*30)
        i += 8
forecast(2)
tuichu=input('输入任意退出')
#英文版
#print('英文版')
#while i<39:
#        #2,10,18,26,34
#    print('day:'+str(data['list'][i]['dt_txt']))
#    print('temp:'+str(data['list'][i]['main']['temp'])+'℃')
#    print('situation:'+str(data['list'][i]['weather'][0]['description']))
#    print('pressure:'+str(data['list'][i]['main']['pressure'])+'hPa')
#    print('the max temp:'+str(data['list'][i]['main']['temp_max'])+'℃')
#    print('the min temp:'+str(data['list'][i]['main']['temp_min'])+'℃')
#    print('*'*30)
#    i+=8
