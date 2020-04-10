#!/usr/bin/python
import os
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer
PORT_NUMBER = int(os.environ.get('PORT', 8084))

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
 
  # GET
  def do_HEAD(self):
        # Send response status code
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        return
  # GET
  def do_GET(self):
        # Send response status code
        self.send_response(200)
 
        # Send headers
        self.send_header('Content-type','text/html')
        self.end_headers()
 
        # Send message back to client
        message = "TEST PAGE1"
        logging.info('PRINT PAGE')
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return
 
def run():
  print('starting server...')
  logging.basicConfig(level=logging.INFO)
  logging.info('Starting httpd...\n')
  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('0.0.0.0', PORT_NUMBER)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()
  
run()