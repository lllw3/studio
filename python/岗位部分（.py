# -*- coding: utf-8 -*-
"""
Created on Mon May 25 10:23:00 2020

@author: Lenovo
"""
#职位信息
"""
<div class="tBorderTop_box">
    <h2><span class="bname">职位信息</span></h2>
    <div class="bmsg job_msg inbox">
        <p>1、协助获取、汇总、更新客户有关信息数据资料，建立项目档案数据库；</p><p>2、协助新项目需求的传达及实施进度跟进；</p><p>3、完成领导交办指定项目的相关事宜，如安排供应商来访安排及接待等事宜；</p><p>4、组织/协助项目招标流程，学习组织撰写和审核工作；</p><p>5、担部门日常管理。如：文件收发、举办大型活动、部门例会管理、维护国际关系等。</p><p><br></p><p>任职要求：</p><p>1、本科以上学历，俄语专业，具有商务俄语应用以及演艺等相关工作经验者优先；</p><p>2、俄语、英语功底好，普通话、粤语流利，熟悉电脑操作；</p><p>3、具有良好的沟通能力和执行能力，保密意识强、能承受一定的工作压力。</p>
                <div class="mt10">
                                        <p class="fp"><span class="label">职能类别：</span><a class="el tdn" href="https://jobs.51job.com/guangzhou-pyq/eyufanyi/">俄语翻译</a></p>
                                </div>
        <div class="share"><a track-type="jobsButtonClick" event-type="6" class="a" href="javascript:void(0);" onclick="weixinMa();">微信分享</a><div id="weixinMa_fx" style="display:none;"><img width="198" height="198" alt="二维码" org="https://jobs.51job.com/wx_qrcode.php?url=https%3A%2F%2Fm.51job.com%2Fsearch%2Fjobdetail.php%3Fjobid%3D118915349"></div>
        </div>
        <div class="clear"></div>
    </div>
</div>
"""
# 联系方式
"""
<div class="tBorderTop_box">
        <h2><span class="bname">联系方式</span></h2>
        <div class="bmsg inbox">
                                                    <p class="fp"><span class="label">上班地址：</span>长隆旅游度假区</p>
                                    <a track-type="jobsButtonClick" event-type="7" class="icon_b i_map" href="javascript:void(0);" onclick="showMapIframe('https://search.51job.com/jobsearch/bmap/map.php?jobid=118915349', '长隆旅游度假区');return false;">地图</a>
                                        <div class="clear"></div>
        </div>
    </div>
"""
#部门消息或公司消息
"""
<div class="tBorderTop_box">
        <h2><span class="bname">部门信息</span></h2>
        <div class="bmsg inbox"><span class="label">所属部门：</span>集团总部<br>
                    </div>
    </div>
"""
import scrapy
from bs4 import BeautifulSoup
# import requests
from lxml import etree
import html
# url='https://jobs.51job.com/guangzhou/118915349.html'
# header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
# response = requests.get(url,header)
# response.encoding = 'utf-8'
# data = response.content.decode('gbk')
def get(self,data):
    selector = etree.HTML(data)
    #直接获取所需部分文字
    # x=selector.xpath('string(/html/body/div[3]/div[2]/div[3]/div[1])') 
    # y=selector.xpath('string(/html/body/div[3]/div[2]/div[3]/div[2])') 
    # z=selector.xpath('string(/html/body/div[3]/div[2]/div[3]/div[3])')

    #获取职业消息部分源码
    first=selector.xpath('//div[@class="tBorderTop_box"][1]')[0]
    first_str=etree.tostring(first).decode('gbk')
    first_c=html.unescape(first_str)
    #获取联系方式部分源码
    second=selector.xpath('//div[@class="tBorderTop_box"][2]')[0]
    second_str=etree.tostring(second).decode('gbk')
    second_c=html.unescape(second_str)
    #定位公司消息、部门消息源码
    third=selector.xpath('//div[@class="tBorderTop_box"][3]')[0]
    #判断有无公司消息
    thirdtitle=selector.xpath('/html/body/div[3]/div[2]/div[3]/div[3]/h2/span')
    thirdt=thirdtitle[0].xpath('string(.)')
    if thirdt !='公司消息':
        # print(str(x))
        # print(str(y))
        # print(str(z))
        third_str=etree.tostring(third).decode('gbk')
        third_c=html.unescape(third_str)
        print(first_c)
        print(second_c)
        print(third_c)
    else:
            # print(str(x))
            # print(str(y))
            print(first_c)
            print(second_c)

