
import requests
import json

link = "http://attic.fineberg.net:33433"
f = requests.get(link)
#print "Attic:\n", f.text
attic = json.loads(f.text)

link = "http://basement.fineberg.net:33433"
f = requests.get(link)
#print "Basement:\n", f.text
basement = json.loads(f.text)

file = open("temphum-vals", "a")
str = str(attic['tempf']) + "," + str(attic['humidity']) + "," + str(basement['tempf']) + "," + str(basement['humidity'])+"\n"
file.write(str)

print "attic\t\tbasement"
print "temp\thum\ttemp\thum"
print attic['tempf'],  "\t", attic['humidity'], "\t", basement['tempf'], "\t",  basement['humidity']
