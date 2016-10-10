
import requests

link = "http://attic.fineberg.net:33433"
f = requests.get(link)
print "Attic:\n", f.text
link = "http://basement.fineberg.net:33433"
f = requests.get(link)

print "Basement:\n", f.text
