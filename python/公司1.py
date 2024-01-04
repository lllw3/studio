# -*- coding: utf-8 -*-
"""
Created on Wed May 20 11:05:45 2020

@author: Lenovo
"""
import urllib.request
import requests
from lxml import etree
import re
from bs4 import BeautifulSoup
from lxml.html import tostring
from lxml.html import fromstring, tostring
from bs4 import BeautifulSoup as bs
from lxml import html
url='https://jobs.51job.com/xian/122218532.html?s=04'
header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
response = requests.get(url,header)
response.encoding = 'utf-8'
data = response.content.decode('gbk')
selector = etree.HTML(data)
#k=selector.xpath('/html/body/div[3]/div[2]/div[3]/div')[0]
#original_html = tostring(k)
#print(k)
k=[]
k.append(re.findall(r'<div class="tBorderTop_box">(.*?)<div class="mt10">',str))
for i in range(0,len(k)):
    print(str(k[i]))


#<div class="tBorderTop_box">
#    <h2><span class="bname">职位信息</span></h2>
#    <div class="bmsg job_msg inbox">
#        职位描述：<br>1、根据法律法规对于字节跳动各平台的商品信息进行审核和标注；<br>2、与质检、复审团队合作，及时处理争议案例，不断优化团队业务指标，提升客户平台服务体验，<br>3、总结和分析审核数据，预判风险，迭代优化审核规则，提升运营效率；<br>4、联动产品、运营等相关部门不断优化和提升风险防控机制体系。<br>职位要求：<br>1、国家统招专科以上学历，专业不限；<br>2、具备强烈的责任心和结果导向，能够在高压环境下工作；<br>3、善于发现、提炼和归纳问题，并提出解决问题的方法；<br>4、有内容风控、广告风控、电商治理、游戏风控等行业经验者优先。
#                <div class="mt10">
#                                        <p class="fp"><span class="label">职能类别：</span><a class="el tdn" href="https://jobs.51job.com/xian/shenheyuan/">审核员</a></p>
#                                </div>
#        <div class="share"><a track-type="jobsButtonClick" event-type="6" class="a" href="javascript:void(0);" onclick="weixinMa();">微信分享</a><div id="weixinMa_fx" style="display:none;"><img width="198" height="198" alt="二维码" org="https://jobs.51job.com/wx_qrcode.php?url=https%3A%2F%2Fm.51job.com%2Fsearch%2Fjobdetail.php%3Fjobid%3D122218532"></div>
#        </div>
