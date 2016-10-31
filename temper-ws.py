#! /usr/bin/env python
#temper-ws
#
# A RESTful web service for accesing the USB temperHUM device
#
# Sam Fineberg sam@fineberg.net
# September 2016
#
# added this line to /etc/udev/rules.d/99-com.rules in order to make temperhum accessible to non-root
# ATTRS{idVendor}=="0c45", ATTRS{idProduct}=="7402", SUBSYSTEMS=="usb", ACTION=="add", MODE="0666", GROUP="plugdev"
#
#9/29/16
#many assumptions, single device only for now.
#fixed static ip, broke up methods
#

import json
import time
from subprocess import call, check_output

# Python's bundled WSGI server
from wsgiref.simple_server import make_server

class temphum:
    #temper_command = ["/usr/local/bin/tempered", "-s", "Fahrenheit"]
    temp = 0.0
    hum = 0.0
    dew = 0.0

    def __init__(self):
	self.read_device("Fahrenheit")
    
    def read_device(self, scale):
	#fp = open('out', 'r')
	#string = fp.read()
    	temper_command = ["/usr/local/bin/tempered", "-s", scale]

	error = 0
	while (error < 10):
           try:
	      string = check_output(temper_command)
              self.parse_output(string)
	      break
	   except:
	      error = error + 1
              time.sleep(1)
	      print "retry.."
	if (error >= 10): raise

#parse output and write to class/object properties
    def parse_output(self, string):
	split = string.split(' ')
	print string
	print split
	print 'temperature', split[3]
#remove % sign and comma
	humidity=split[7].replace('%', '')
	humidity=humidity.replace(',', '')
	print 'humidity', humidity 
	print 'dew point', split[10]
#write values out
	self.temp=float(split[3])
	self.hum=float(humidity)
	self.dew=float(split[10])


def json_ws (environ, start_response):
    th.read_device("Fahrenheit")
    obj = {
      	'humidity' : th.hum,
        'tempf' : th.temp,
        'dewf' : th.dew,
    	}
    th.read_device("Celsius");
    obj.update ({ 'tempc' : th.temp, 'dewc' : th.dew, })

    response_body = json.dumps(obj, indent=4, sort_keys=True)
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]
    start_response(status, response_headers)
    return response_body


# Instantiate the server
httpd = make_server (
#    'localhost', # The host name
    '0.0.0.0', # The host name
    33433, # A port number where to wait for the request
    json_ws, # The application object name, in this case a function
)

#Instantiate the temperhum device object
#th = temphum()
error = 0
while (error < 10):
   try:
      th = temphum()
      break
   except:
      error = error + 1
      print "retry.."
if (error >= 10): raise

# Wait for a single request, serve it and do it again forever
while  True: 
   try:
      httpd.handle_request()
   except:
      pass
