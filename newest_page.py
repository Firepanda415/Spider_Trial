# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 13:57:18 2017

@author: hazhou
"""

from bs4 import BeautifulSoup
import requests

def get_newest():
    url = 'http://jandan.net/ooxx'
    headers = {
                "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }
    request = requests.get(url = url, headers = headers)
    request.encoding = 'utf-8'
    html = request.text
    soup = BeautifulSoup(html,'lxml')
    newest_page = (soup.find_all(class_ = 'current-comment-page', limit=1))
    page = newest_page[0].string[1:-1]
    return int(page)
    
if __name__ == '__main__':
    get_newest()