from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return 'Esta app usa la app de Last.fm ;)'

@app.route('/artist/<artist>')
def get_artists(artist):
    # artist = artist
    url = 'http://ws.audioscrobbler.com/2.0/'
    lang = 'es'
    args = {
        'method': 'artist.getinfo',
        'artist': artist,
        'api_key': '4e8c16304446243a2a3d4b365a98e791',
        'format': 'json',
        'autocorrect': '1',
        'lang': lang
    }

    response = requests.get(url, params=args)
    print(response)
    print(response.url)

    if response.status_code == 200:
        content_json = response.json()
        content = response.content
        bio = content_json['artist']['bio']['summary']
        return(bio)

if __name__ == "__main__":
    app.run(debug=True, port=7000)
