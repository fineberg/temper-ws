
import requests
import json
import subprocess
import datetime

link = "http://attic.fineberg.net:33433"
f = requests.get(link)
#print "Attic:\n", f.text
attic = json.loads(f.text)

link = "http://basement.fineberg.net:33433"
f = requests.get(link)
#print "Basement:\n", f.text
basement = json.loads(f.text)

string = datetime.datetime.now().isoformat()

file = open("/home/sam/temphum-vals", "a")
str = string+","+str(attic['tempf']) + "," + str(attic['humidity']) + "," + str(basement['tempf']) + "," + str(basement['humidity'])+"\n"
file.write(str)

print "attic\t\tbasement"
print "temp\thum\ttemp\thum"
print attic['tempf'],  "\t", attic['humidity'], "\t", basement['tempf'], "\t",  basement['humidity']
