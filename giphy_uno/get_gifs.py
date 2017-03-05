
import requests

tag = raw_input('Tag')
url = 'http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=%s' % (tag)

r = requests.get(url)

if r.status_code == 200:
     data = r.json()
     print(data['data']['url'])
else:
    print('No hay nada')
