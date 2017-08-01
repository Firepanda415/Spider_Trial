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

def grab(start_page,ending_page, lim, amount):  
    
    if start_page == "" or ending_page == "":
        print("Please Check Your Input(s)!!!")
        return
    
    print("Start from page " + str(start_page) + " to page " + str(ending_page))
    
    if not isinstance(start_page,int):
        start_page = int(start_page)     
    if not isinstance(ending_page,int):
        ending_page = int(ending_page)
        
    list_url = []
    spacing = -1
    if start_page < ending_page:
        spacing = 1
    
    exit_flag=0
    for num in range(start_page,ending_page,spacing): #Start from page 194 to 190, about 100 pics
        url = 'http://jandan.net/ooxx/page-%s#comments' % num
        headers = {
                "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }
        req = requests.get(url = url,headers = headers) #Send request to obtain page information
        req.encoding = 'utf-8'
        html = req.text
        bf = BeautifulSoup(html, 'lxml') #Sort the page text
        #targets_url = bf.find_all(class_='view_img_link') #Find the links of all pics
        if not lim:
            targets_url = bf.find_all(class_='view_img_link')
            for each in targets_url:
                list_url.append('http:' + each.get('href')) #Rewrite the link infor
        else:
            targets_url = bf.find_all(class_='view_img_link', limit=amount)
            for each in targets_url:
                if len(list_url) < amount:
                    list_url.append('http:' + each.get('href')) #Rewrite the link infor
                else:
                    exit_flag=1
                    break
            
        if exit_flag:
            break

    print('Obtained all links')
    
    filenum = 1
    for each_img in list_url:
        img_info = each_img.split('.')
        filetype = '.' + img_info[-1]
        filename = str(filenum) + filetype
        print('Start Downloading: ' + filename)
        
        #Download all pics to folder named 'images', create one automatically if not exists
        if 'images' not in os.listdir():
            os.makedirs('images')
        
        #Download the pics
        urlretrieve(each_img,'images/'+filename)
        
        filenum += 1
        time.sleep(1)#Stop 1 sec to pretend like a human
        
    print('Complete!')

if __name__ == '__main__':
    grab(200,199,True,1)