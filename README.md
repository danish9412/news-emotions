# News Emotions Analyzer
Specifically developed as a backend application for Stock Prediction Model using Machine Learning.
But It can be used as a standalone application as well

## File Structure
- NewsEmotions.py has google news fetcher and Watson tone anlyzer
- server.py has flask server for REST calls

## Starting application
- Create a config.ini file in the root folder for API key. As mentioned below:

[config]
key = **Your API key**

- Run server.py
- Make POST call to http://127.0.0.1:8081 with "stockName" parameters in body (Stick to NASDAQ naming convention for precise results) 
