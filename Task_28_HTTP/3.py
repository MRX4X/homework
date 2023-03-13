import requests
r=requests.get('https://rickandmortyapi.com/api/character').json()
print('Имя', r['results'][0]['name'], 'планета', r['results'][0]['location']['name'])