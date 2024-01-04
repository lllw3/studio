# -*- coding: utf-8 -*-
"""
Created on Sun May 17 13:40:51 2020

@author: Lenovo
"""

import random
import requests
from bs4 import BeautifulSoup
import urllib
import os
 
 
BASE_URL = 'https://www.doutula.com/photo/list/?page='
URL_LIST = []

for x in range(750,755):
    REAL_URL = BASE_URL+str(x)
    URL_LIST.append(REAL_URL)
 
def get_url(url,k):
    my_headers = [
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)",
    ]
    header = {
        "User-Agent": random.choice(my_headers)
    }
    re = requests.get(url, headers=header)
    soup = BeautifulSoup(re.content, "lxml")
    IMG_LIST = soup.find_all('img', 'img-responsive lazy image_dta')
    for img in IMG_LIST:
        imgurl = img['data-original']
        
        pic=requests.get(imgurl,headers=header).content
        with open('f:\imkyy'+str(k)+'.jpg','wb')as f:
            f.write(pic)
            k=k+1
            print(str(k)+'完成')
def main():
    k=55712
    for url in URL_LIST:
        get_url(url,k)
        
 
if __name__ == '__main__':
    main()
