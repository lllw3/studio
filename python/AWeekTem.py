# -*- coding: utf-8 -*-
"""
Created on Wed May  6 21:39:18 2020

@author: Lenovo
"""
#定义列表打印一周温度
#1. 定义一个天气列表(list类型)。写出里面一周每个温度(数字类型)
#2. 打印出5天的天气(print)，打印内容为 星期一XX度(数据拼接)
day=['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
tem=[19,33,-2,24,17,10,-24]
for num in range(0,7):
   print(day[num]+str(tem[num])+'度')
print('星期三温度是'+str(tem[2])+'度')

#拓展 计算一周温度的平均温度
ave=sum(tem)/7
print("一周平均温度是%0.2f"%ave+'度')
# 原创列表推导式 计算一周温度的平均温度
print('一周平均温度是'+str(sum([tem[i] for i in range(len(tem))])/7)+'度')
