# import requests
# r=requests.get('https://rickandmortyapi.com/api/character').json()
# q=requests.get('https://rickandmortyapi.com/api/episode').json()
# print('Имя', r['results'][0]['name'], 'планета', r['results'][0]['location']['name'])
# ids=r['results'][0]['id']
# ids_last=r['results'][19]['id']
# for i in range(ids, ids_last):
#     print(q['results'][ids+1]['characters'])

import requests
r=requests.get('https://rickandmortyapi.com/api/character').json()
# print(r)
# print('Имя', r['results'][0]['name'], 'планета', r['results'][0]['location']['name'])
ids=r['results'][0]['id']
ids_last=r['results'][ids*5]['id']

for i in range(ids, ids_last):
    if ids==ids_last:
        print('Имя', r['results'][ids_last]['name'], 'планета', r['results'][ids_last]['location']['name'], r['results'][ids_last]['episode'])
    print('Имя', r['results'][ids]['name'], 'планета', r['results'][ids]['location']['name'], r['results'][ids]['episode'])
    ids+=1
