# -*- coding: utf-8 -*-
"""
Created on Tue May 12 16:53:58 2020

@author: Lenovo
"""



from lxml import etree
#import urllib.request
import requests
import csv
#import re

url = 'https://live.aicai.com/pages/jsbf/jczq.shtml'

#agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
html=requests.get('https://live.aicai.com/pages/jsbf/jczq.shtml', headers=headers)
tree = etree.HTML(html.text)
trTags = tree.xpath('//*[@id="jq_jsbf_body"]/tbody[2]/text()')
#trTags = tree.xpath('//*[@id="jq_league_matchTime_1676269"]/text()')
items=[]
for tag in trTags:
    try:
        item = []
        item.append(tag.xpath('./td[3]/text()')[0])
        #item.append(tag.xpath('./td[3]/a/text()')[0])
        #item.append(tag.xpath('./td[4]/text()')[0])
        #item.append(tag.xpath('./td[5]/text()')[0])
        #item.append(tag.xpath('./td[5]/a/text()')[0])
        #item.append(tag.xpath('./td[5]/text()')[0])
        #item.append(tag.xpath('./td[6]/text()')[0])
        #item.append(tag.xpath('./td[7]/text()')[0])
        items.append(item)
        item=[]
    except:
       pass
#return items

#file_name = 'basketball.csv'
#with open(file_name, 'a', errors='ignore', newline='',encoding='utf-8') as f:
#    f_csv = csv.writer(f)
#    f_csv.writerows(items)
#    print('写入完毕')
#with open(file_name, mode='r', encoding='utf-8') as f:
##    f.read()
import json
filename = 'F:\scrape_data.json'
with open(filename, 'r') as fd:
    json_str = fd.read()
    data = json.loads(json_str)

print(data['2019-04-16']["0"])
print(data['2019-04-16']["1"])