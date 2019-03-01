#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 16:55:00 2019

@author: danishsiddiqui
"""

from flask import Flask
from flask import request
from flask import jsonify
import NewsEmotions
 
app = Flask(__name__)
# HTTPRequestHandler class
class httpServer():
 
    @app.route('/', methods=['GET','POST'])
    def parse_request():
        #data = request.data  # data is empty
        stockName = request.form.get('stockName')
        #print("stockName",stockName)
        newsArray = []
        newsArray = NewsEmotions.google_news_grabber(stockName)
        
        respArray = []
        for news in newsArray:
            singleTitle = news.replace(".", "")
            toneJSON = NewsEmotions.tone_analyzer(singleTitle)
            if(toneJSON != None):
                respArray.append(toneJSON)
            
        resp = jsonify(respArray)
        return resp
    
    if __name__ == "__main__":
        app.debug = True
        app.run(host = '0.0.0.0',port=5000)
#NewsEmotions.tone_analyzer("Its an amazing day") 