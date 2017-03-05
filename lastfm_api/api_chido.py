import requests

if __name__ == '__main__':

    artist_default = 'Justice'
    # artist = raw_input('Artista? ')
    lang_default = 'es'
    # lang = raw_input('Idioma? (es/en) ')
    url = 'http://ws.audioscrobbler.com/2.0/'
    args = {
        'method': 'artist.getinfo',
        'artist': artist_default,
        'api_key': '4e8c16304446243a2a3d4b365a98e791',
        'format': 'json',
        'autocorrect': '1',
        'lang': lang_default
    }
    # 'limit': '3',

    response = requests.get(url, params=args)
    print(response)
    print(response.url)

    if response.status_code == 200:
        content_json = response.json()
        content = response.content
        bio = content_json['artist']['bio']['summary']
        print(bio)
        # print(content_uno['artist']['similar']['artist'][1]['name'])
        # print(content.keys())
        similar_artists = []
        for similares in content_json['artist']['similar']['artist']:
            similar = similares['name']
            similar_artists.append(similar)
        for artist in similar_artists:
            print artist
            
if __name__ == "__main__":
    app.run(debug=True, port=7000)
