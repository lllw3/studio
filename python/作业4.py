# -*- coding: utf-8 -*-
"""
Created on Wed May 20 15:25:47 2020

@author: Lenovo
"""

import urllib
import urllib.request
import requests
import re
from bs4 import BeautifulSoup
url='https://jobs.51job.com/all/co5423733.html#syzw'
header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
response = requests.get(url,header)
response.encoding = 'utf-8'
data = response.content.decode('gbk')
zhiwei=re.findall()
    
