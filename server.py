#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 16:55:00 2019

@author: danishsiddiqui
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import NewsEmotions
 
# HTTPRequestHandler class
class httpServer_RequestHandler(BaseHTTPRequestHandler):
 
  # GET
  def do_GET(self):
        # Send response status code
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()
 
        # Send message back to client
        message = "Hello world!"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return
 
def run():
 
  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('127.0.0.1', 8081)
  httpd = HTTPServer(server_address, httpServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()
 
NewsEmotions.tone_analyzer("Its an amazing day") 
#run()