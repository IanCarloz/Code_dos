import requests
import json

if __name__ == '__main__':

    url = 'http://httpbin.org/get'
    args = {
        'hola': 'ke_ase',
        'oshe': 'bais'
    }

    response = requests.get(url, params=args)
    print(response)
    print(response.url)

    if response.status_code == 200:
        response_json_uno = response.json() # Dicionario
        response_json_dos = json.loads(response.text) # usa libreria json
        hola = response_json_uno['args']['hola']
        print(hola)
