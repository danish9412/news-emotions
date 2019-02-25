#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 15:58:08 2019

@author: danishsiddiqui
"""
import requests
from bs4 import BeautifulSoup
from watson_developer_cloud import ToneAnalyzerV3
import configparser
import json

config = configparser.ConfigParser()
config.read("/Users/danishsiddiqui/Projects/StockNews/config.ini")
key = config.get('config','key')
#print("key: ",key)

def tone_analyzer(text):
    tone_analyzer = ToneAnalyzerV3(
      version='2017-09-21',
      iam_apikey=key,
      url='https://gateway.watsonplatform.net/tone-analyzer/api'
    )    
    tone_analysis = tone_analyzer.tone(
        {'text': text},
        'application/json'
    ).get_result()
    print(json.dumps(tone_analysis, indent=4, sort_keys=True))

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
#google_news_grabber('NFLX')  

text = 'Team, I know that times are tough! Product '\
        'sales have been disappointing for the past three '\
        'quarters. We have a competitive product, but we '\
        'need to do a better job of selling it!'
tone_analyzer(text)