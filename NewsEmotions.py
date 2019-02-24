#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 15:58:08 2019

@author: danishsiddiqui
"""
import requests
from bs4 import BeautifulSoup

def google_news_grabber(stockName):
    #stockNameEncoded = urllib.parse.quote_plus(stockName)
    print("stockName: ",stockName);
    url = 'https://news.google.com/rss/search?q='+stockName+'&hl=en-US&gl=US&ceid=US:en'
    response = requests.get(url)
    page = response.content
    #print("page: ",page);
    soup = BeautifulSoup(page, 'html.parser')
    filtered = soup.find_all('title')
    #print("filtered: ",filtered[3].text)
    newsArray = []
    for news in filtered:
        #print("filtered: ",news.text)
        paragraphs = news.text
        newsArray.append(paragraphs)
    
    print("newsArray: ",newsArray[2])
google_news_grabber('NFLX')   