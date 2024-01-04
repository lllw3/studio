#!/usr/bin/env python
# coding: utf-8

# ## 共享cookie池

# In[ ]:


from flask import Flask,request
from json import dumps
import json
import pyautogui
import time
from redis import StrictRedis
pyautogui.FAILSAFE = False
#服务器的地址，端口
r = StrictRedis(host='127.0.0.1',port=6379,decode_responses=True)#decode_responses=True 返回数据都是字符串
app = Flask(__name__)

@app.route('/')
def names():
    name = request.args.get('name','')
    autcode = request.args.get('autcode','')
    if name == '':
        return dumps(r.hgetall('names'))
    else:
        return r.hget('names',name)

@app.route('/autcodes')
def autcodes():
    name = request.args.get('name','')
    autcode = request.args.get('autcode','')
    
    if name!='' and autcode!='':
        r.hset('autcodes',name,autcode)
    
    return dumps(r.hgetall('autcodes'))

@app.route('/order')
def order():
    try:
        order_url = json.loads(request.data)['url']
        r.sadd('order_urls',order_url)
    except Exception as err:
        pass
    return dumps(list(r.smembers('order_urls')))

app.run(host='0.0.0.0',port=80)#121.36.62.129


# In[ ]:




