# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 13:14:30 2017

@author: zhengm
"""

from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import requests
import os
import time

if __name__ == '__main__':
    list_url = []
    for num in range(194,190,-1): #Start from page 194 to 190, about 100 pics
        url = 'http://jandan.net/ooxx/page-%s#comments' % num
        headers = {
                "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }
        req = requests.get(url = url,headers = headers) #Send request to obtain page information
        req.encoding = 'utf-8'
        html = req.text
        bf = BeautifulSoup(html, 'lxml') #Sort the page text
        targets_url = bf.find_all(class_='view_img_link') #Find the links of all pics

        for each in targets_url:
            list_url.append('http:' + each.get('href')) #Rewrite the link infor

    print('Obtained all links')
    
    filenum = 1
    for each_img in list_url:
        img_info = each_img.split('.')
        filetype = '.' + img_info[-1]
        filename = str(filenum)+filetype
        print('Start Downloading: ' + filename)
        
        #Download all pics to folder named 'images', create one automatically if not exists
        if 'images' not in os.listdir():
            os.makedirs('images')
        
        #Download the pics
        urlretrieve(each_img,'images/'+filename)
        
        filenum = filenum + 1
        time.sleep(1)#Stop 1 sec to pretend like a human
        
    print('Complete!')