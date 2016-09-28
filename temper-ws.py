#! /usr/bin/env python
import json
from subprocess import call, check_output

# Python's bundled WSGI server
from wsgiref.simple_server import make_server

class temphum:
    temp = 0.0
    hum = 0.0
    dew = 0.0

    def __init__(self):
	response = check_output("date")
	#response = check_output("/usr/local/bin/tempered", "-s", "Fahrenheit")
	self.temp = 77
	self.hum = 43
	self.dew = 99
	print response
    
    def read_device(self):
	fp = open('out', 'r')
	string = fp.read()
	split = string.split(' ')
	print string
	print split
	print 'temperature', split[3]
	humidity=split[7].replace('%', '')
	humidity=humidity.replace(',', '')
	print 'humidity', humidity 
	print 'dew point', split[10]
	self.temp=float(split[3])
	self.hum=float(humidity)
	self.dew=float(split[10])


def json_ws (environ, start_response):
    th = temphum()
    th.read_device()
    obj = {
        "temperature" : th.temp,
      	"humidity" : th.hum,
        "dewpoint" : th.dew,
    	}
    response_body = json.dumps(obj, indent=4, sort_keys=True)
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]
    start_response(status, response_headers)
    return [response_body]


# Instantiate the server
httpd = make_server (
    'localhost', # The host name
    8051, # A port number where to wait for the request
    json_ws, # The application object name, in this case a function
)

# Wait for a single request, serve it and quit
while  True: httpd.handle_request()
