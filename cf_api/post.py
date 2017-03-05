import requests
import json

if __name__ == '__main__':

    url = 'http://httpbin.org/post'
    payload = {
        'hola': 'ke_ase',
        'oshe': 'bais'
    }

    response_1 = requests.post(url, json=payload) # Con json, post se encarga de serializarlos
    response_2 = requests.post(url, data=payload) # lo manda a form 
    response_3 = requests.post(url, data=json.dumps(payload)) # Con data, yo debo serializarlos

    print(response_1)
    print(response_2)
    print(response_3)

    print(response_1.url)
    print(response_2.url)
    print(response_3.url)

    print(response_1.content)
    print(response_2.content)
    print(response_3.content)
