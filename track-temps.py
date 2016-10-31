
import requests
import json
import subprocess
import datetime

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

string = datetime.datetime.now().isoformat()

file = open("/home/sam/temphum-vals", "a")
str = string+","+str(attic['tempf']) + "," + str(attic['humidity']) + "," + str(basement['tempf']) + "," + str(basement['humidity'])+"\n"
file.write(str)

print "attic\t\tbasement"
print "temp\thum\ttemp\thum"
print attic['tempf'],  "\t", attic['humidity'], "\t", basement['tempf'], "\t",  basement['humidity']
