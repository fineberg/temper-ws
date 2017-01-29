
import requests
import json
import subprocess
import time
import datetime

import socket

def netcat(hostname, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Connect to ", hostname, " port ", port
    s.connect((hostname, port))
    print "sending "+content
    s.sendall(content)
    s.shutdown(socket.SHUT_WR)
    print "Connection closed."
    s.close()

graphite_host = "graphite.fineberg.net"
graphite_port = 2003

errors = 0
ok = False
while (not ok) and (errors < 10) :
   link = "http://attic.fineberg.net:33433"
   try :
      f  = requests.get(link)
#      print "Attic:\n", f.text
      attic = json.loads(f.text)
      if (attic['humidity'] < 0) or (attic['tempf'] < 0): 
         ok=false
      else: 
         ok = True

      break
   except:
      print "try again... Attic:\n", f.text
      errors = errors + 1
  
if (errors >= 10): raise
 
ok = False
errors = 0
while (not ok) and (errors < 10) :
   link = "http://basement.fineberg.net:33433"
   try: 
      f = requests.get(link)
#      print "Basement:\n", f.text
      basement = json.loads(f.text)
      if (basement['humidity'] < 0) or (basement['tempf'] < 0): 
         ok=false
      else: 
         ok = True
      break	
   except:
      print "try again... basement:\n", f.text
      errors = errors + 1

if (errors >= 10): raise

ok = False
errors = 0
while (not ok) and (errors < 10) :
   link = "http://outdoor.fineberg.net:33433"
   try: 
      f = requests.get(link)
#      print "Basement:\n", f.text
      outdoor = json.loads(f.text)
      if (outdoor['tempf'] < 0): 
         ok=false
      else: 
         ok = True
      break	
   except:
      print "try again... outdoor:\n", f.text
      errors = errors + 1

if (errors >= 10): raise

datestring = str(int(time.time()))

strout = "temphum.attic.tempc "+str(attic['tempc']) + " " + datestring+"\n"
print strout
netcat(graphite_host, graphite_port, strout)
strout = "temphum.attic.tempf "+str(attic['tempf']) +  " " +datestring+"\n"
print strout
netcat(graphite_host, graphite_port, strout)
strout = "temphum.attic.humidty "+str(attic['humidity']) +  " " +datestring+"\n"
print strout
netcat(graphite_host, graphite_port, strout)
strout = "temphum.attic.dewc "+str(attic['dewc']) +  " " +datestring+"\n"
print strout
netcat(graphite_host, graphite_port, strout)
strout = "temphum.attic.dewf "+str(attic['dewf']) +  " " +datestring+"\n"
print strout
netcat(graphite_host, graphite_port, strout)

strout = "temphum.basement.tempc "+str(basement['tempc']) + " " + datestring+"\n"
print strout
netcat(graphite_host, graphite_port, strout)
strout = "temphum.basement.tempf "+str(basement['tempf']) +  " " +datestring+"\n"
print strout
netcat(graphite_host, graphite_port, strout)
strout = "temphum.basement.humidty "+str(basement['humidity']) +  " " +datestring+"\n"
print strout
netcat(graphite_host, graphite_port, strout)
strout = "temphum.basement.dewc "+str(basement['dewc']) +  " " +datestring+"\n"
print strout
netcat(graphite_host, graphite_port, strout)
strout = "temphum.basement.dewf "+str(basement['dewf']) +  " " +datestring+"\n"
print strout
netcat(graphite_host, graphite_port, strout)

strout = "temphum.outdoor.tempc "+str(outdoor['tempc']) + " " + datestring+"\n"
print strout
netcat(graphite_host, graphite_port, strout)
strout = "temphum.outdoor.tempf "+str(outdoor['tempf']) +  " " +datestring+"\n"
print strout
netcat(graphite_host, graphite_port, strout)
strout = "temphum.outdoor.humidty "+str(outdoor['humidity']) +  " " +datestring+"\n"
print strout
netcat(graphite_host, graphite_port, strout)
strout = "temphum.outdoor.dewc "+str(outdoor['dewc']) +  " " +datestring+"\n"
print strout
netcat(graphite_host, graphite_port, strout)
strout = "temphum.outdoor.dewf "+str(outdoor['dewf']) +  " " +datestring+"\n"
print strout
netcat(graphite_host, graphite_port, strout)
