
import requests
import json

link = "http://attic.fineberg.net:33433"
f = requests.get(link)
print "Attic:\n", f.text
attic = json.loads(f.text)

link = "http://basement.fineberg.net:33433"
f = requests.get(link)
print "Basement:\n", f.text
basement = json.loads(f.text)

print "Attic temp: ", attic['tempf']
print "Basement temp", basement['tempf']
