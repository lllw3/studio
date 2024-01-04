# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 18:40:34 2020

@author: Lenovo
"""
import json
file=r'C:\Users\Lenovo\.spyder-py3\batch_shop_demo.json'
#商铺名，店铺id，营业状态，省份，城市，平台分类，地址，经纬度，店铺订单量，联系方式，营业时间，
#店铺优惠，店铺链接，评分，评论数，
#店铺优惠另取 营业状态找不到
#新：名字，地址，优惠，电话
with open (file,'r',encoding='utf-8') as f:
     load_dict = json.load(f)
     #print(load_dict)
    
# "name":"鲍喜鲍鱼饭·炖品(广州荔湾店)"
name=load_dict['rst']['name']#名

#"id":"E11022687882350934983",
ID=load_dict['rst']['id']#id

lianjie='https://h5.ele.me/shop/#id='+ID#链接

#"address":"广州市荔湾区小梅大街2号二层123房"
address=load_dict['rst']['address']
city=address[0:3]

#"phone":null
phone=load_dict['rst']['phone']#电话

shop={'商铺名':name,'店铺ID':ID,'地址':address,
      '联系方式':phone,'店铺链接':lianjie,}
print(shop)

