import requests
r=requests.get('https://rickandmortyapi.com/').text
print(r)