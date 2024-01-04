# -*- coding: utf-8 -*-
"""
Created on Wed May 20 11:01:58 2020

@author: Lenovo
"""
import requests
from lxml import etree
#url='https://jobs.51job.com/foshan-nhq/121513783.html?s=04'
#url='https://jobs.51job.com/xian/122218532.html?s=04'
url='https://jobs.51job.com/guangzhou/118915349.html'
header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
def getmess(url,headers):
    response = requests.get(url,header)
    response.encoding = 'utf-8'
    data = response.content.decode('gbk')
    selector = etree.HTML(data)
    info = {}
    z=selector.xpath('string(/html/body/div[3]/div[2]/div[3]/div[1]/div)')
    l=[]
    for i in range(0,len(z)):
        l.append(z[i])
    info['职位信息']=l
    info['联系方式']=selector.xpath('/html/body/div[3]/div[2]/div[3]/div[2]/div/p/text()')
    info['部门信息']=selector.xpath('/html/body/div[3]/div[2]/div[3]/div[3]/div/text()')
    info['xx']=selector.xpath('/html/body/div[3]/div[2]/div[3]/div[4]/div/text()')
    print(info)
#/html/body/div[3]/div[2]/div[3]/div[1]/div
#/html/body/div[3]/div[2]/div[3]/div[2]/div/p
#/html/body/div[3]/div[2]/div[3]/div[1]/div/p
getmess(url,header)