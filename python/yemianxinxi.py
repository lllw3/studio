# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 16:03:25 2020

@author: Lenovo
"""

from scrapy.selector import Selector
from scrapy.http import HtmlResponse
#url='https://www.epwk.com/task/875055/'
url='https://www.epwk.com/task/874858/'

   # page_url=[]          
  # for j in response:
  #     urls = response.xpath('div/h3/a/@href').extract()
  #     page_url.append(urls)
  # for k in page_url:
  #     page_detail(self,urls)
  #
  
def page_detail(urls):
     responses = HtmlResponse(urls)
            #标题 任务出价 发布者 雇佣进度条 参与要求 任务需求 任务附件 任务情况 招标公司#
     title=responses.selector.xpath('/html/body/div[10]/div/div[1]/div[1]/div[2]/div[1]/text()').extract()
     task_pay=responses.selector.xpath('/html/body/div[10]/div/div[1]/div[3]/div[1]/div/div[2]/div[1]/span[1]/span/text()').extract()
     user=responses.selector.xpath('/html/body/div[10]/div/div[1]/div[3]/div[1]/div/div[1]/span/text()').extract()
     task_progress=responses.selector.xpath('/html/body/div[10]/div/div[1]/div[3]/div[2]//text()').extract()
     task_chenxin=responses.selector.xpath("//div[@class='task-chenxin']//text()").extract()
     task_content=responses.selector.xpath("//div[@class='task-info-content']/text()").extract()   
     affix=responses.selector.xpath("/html/body/div[10]/div/div[1]/div[3]/div[4]/div[1]/div[@class='clearfix pt_10 pb_10']//@href").extract()
     task_user_info_action=responses.selector.xpath("//div[@class='task-user-info-action']//text()").extract()
     task_works=[]
     try:   
           for i in responses.xpath("//*[@id="task_page"]/div"):
               works=responses.selector.xpath("//*[@class="task-work-element-info-action"]/h3/a/@title/text()").extract()
               task_works.append(works)
     except Exception as e:
           pass
     item={}
     item['title']=''.join(title)
     item['task_pay']=''.join(task_pay)#招标任务/雇佣任务（任务出价
     item['user']=''.join(user)#发布者
     #item['task_progress']-''.join(task_progress)#雇佣进度条
     item['task_chenxin']=''.join(task_chenxin)#参与要求
     item['task_content']=''.join(task_content)#任务需求
     item['affix']=''.join(affix)#任务附件
     item['task_user_info_action']=''.join(task_user_info_action)#任务情况
     item['bidder']=','.join(task_works)#竞标公司
     print(item)
page_detail(url)
