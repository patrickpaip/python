import requests
r = requests.get('http://localhost:5000')
a=r.json()
print (a["name"])