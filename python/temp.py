# -*- coding: utf-8 -*-
"""
Spyder 编辑器

这是一个临时脚本文件。
"""
import requests
from lxml import etree 
url = "https://www.epwk.com/task/875055/" 
response = requests.get(url= url) 
wb_data = response.text 
responses= etree.HTML(wb_data) 

def page(responses):
       item={}
       title=responses.xpath('/html/body/div[10]/div/div[1]/div[3]/div[1]/div/div[2]/div[2]/h1/text()')
       task_pay=responses.xpath('normalize-space(/html/body/div[10]/div/div[1]/div[3]/div[1]/div/div[2]/div[1]/span[1]/span/text())')
       user=responses.xpath('/html/body/div[10]/div/div[1]/div[3]/div[1]/div/div[1]/span/text()')
       task_chenxin=responses.xpath("//div[@class='task-chenxin']//text()")
       task_content=responses.xpath("//div[@class='task-info-content']/text()")
       affix=responses.xpath("/html/body/div[10]/div/div[1]/div[3]/div[4]/div[1]/div[@class='clearfix pt_10 pb_10']//@href")
       task_user_info_action=responses.xpath("//div[@class='task-user-info-action']//text()")
       task_works=[]
       try: 
           for i in responses.xpath('//*[@id="task_page"]/div'):
               works=responses.xpath('//[@class="task-work-element-info-action"]/h3/a/@title/text()')
               task_works.append(works)
       except:
           pass
       item['title']=''.join(title)#标题
       item['task_pay']=''.join(task_pay)#招标任务/雇佣任务（任务出价
       item['user']=''.join(user)#发布者
       item['task_chenxin']=''.join(task_chenxin)#参与要求
       item['task_content']=''.join(task_content).replace('\n','')#任务需求
       item['affix']=''.join(affix)#任务附件
       item['task_user_info_action']=''.join(task_user_info_action).replace('\n ','')#任务情况
       item['bidder']=','.join(task_works)#竞标公司
       print(item)
page(responses)