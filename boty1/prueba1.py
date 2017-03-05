# -*- coding: utf-8 -*-

from flask import Flask, request
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def prueba_mensaje():
    msj = json.loads(request.data)
    txt = msj['originalRequest']['data']['message']['text']
    id_usr = msj['originalRequest']['data']['sender']['id']
    # print(msj['originalRequest']['data']['message']['text'])

    url = 'http://ws.audioscrobbler.com/2.0/'
    artist = txt
    args = {
    'method': 'artist.getinfo',
    'artist': artist,
    'api_key': '4e8c16304446243a2a3d4b365a98e791',
    'format': 'json',
    'autocorrect': '1'
    }
    # 'limit': '3',

    response = requests.get(url, params=args)
    print(response)
    print(response.url)

    if response.status_code == 200:
        content_uno = response.json()
        content_dos = response.content
        respuesta = content_uno['artist']['bio']['summary']

    msj_a_fb = requests.post('https://graph.facebook.com/v2.6/me/messages?access_token=EAAaG0SIskZBYBAAyRCSRZBvkAZBk9JFCuTPuMsZAfLo1v2VIwpfOf7ULr5ZAtVZBCKoZBeEyj5VSF2AwjOq8z4iwWkEfGlatSbWvGd3tph92UaXUKXt0aGWrtqnxa317YOEqsyHZBs6wDwBiIeNCW9lDZBhgGPkLZCSCDkxyZBZCEscH3QZDZD',
    headers={'Content-Type': 'application/json'},
    data=json.dumps({'recipient': {'id': id_usr},
    'message': {'text': respuesta}}))
    return('data')

if __name__ == "__main__":
    app.run(debug=True)
