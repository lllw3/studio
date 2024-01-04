# -*- coding: utf-8 -*-
"""
Created on Wed May 20 10:06:08 2020

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
   # z=selector.xpath('string(/html/body/div[3]/div[2]/div[3]/div[1]/div)')
    #获取大标题
    firsttitle=selector.xpath('/html/body/div[3]/div[2]/div[3]/div[1]/h2/span')
    first=firsttitle[0].xpath('string(.)')
    secondtitle=selector.xpath('/html/body/div[3]/div[2]/div[3]/div[2]/h2/span')
    second=secondtitle[0].xpath('string(.)')
    thirdtitle=selector.xpath('/html/body/div[3]/div[2]/div[3]/div[3]/h2/span')
    third=thirdtitle[0].xpath('string(.)')
    num1=selector.xpath('/html/body/div[3]/div[2]/div[3]/div[1]/div')
    z_l=num1[0].xpath('string(.)')#.replace('','')
    #判断是否包含部门信息
    if third != '公司消息':
        #获取内容
        x=selector.xpath('/html/body/div[3]/div[2]/div[3]/div[2]/div/p/text()')
        y=selector.xpath('/html/body/div[3]/div[2]/div[3]/div[3]/div/text()')
        #z=selector.xpath('/html/body/div[3]/div[2]/div[3]/div[3]/div/text()')
        #/html/body/div[3]/div[2]/div[3]/div[3]/div
    #info['xx']=selector.xpath('/html/body/div[3]/div[2]/div[3]/div[4]/div/text()')
        info={first:z_l,second:x,third:y}
    if third == '公司信息':
         x=selector.xpath('/html/body/div[3]/div[2]/div[3]/div[2]/div/p/text()')
         y=selector.xpath('/html/body/div[3]/div[2]/div[3]/div[3]/div/text()')
         info={first:z_l,second:x}
    print(info)
    with open('f:gs.json','w') as f:
        f.write(str(info))
    #return info
getmess(url,header)