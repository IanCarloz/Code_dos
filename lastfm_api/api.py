import requests

artist = 'justice'
key = '4e8c16304446243a2a3d4b365a98e791'

url = 'http://ws.audioscrobbler.com/2.0/?method=artist.getsimilar&artist=%s&api_key=%s&format=json' % (artist, key)

r = requests.get(url)

data =  r.json()

print data['similarartists']['artist'][1]
