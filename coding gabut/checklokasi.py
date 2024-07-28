import socket
import requests
import pprint
import json

hostname = input('masukkan url:')
ip_address = socket.gethostbyname(hostname)

requests_url = 'https://geolocation-db.com/jsonp' + ip_address
response = requests.get(requests_url)
geolocation = response.content.decode()
geolocation = geolocation.split("(")[1].strip(")")
geolocation = json.loads(geolocation)
for k,v in geolocation.items():
    pprint.pprint(str (k) +  ':' + str (v))