import requests
r=requests.get('https://randomuser.me/api/').json()
print('Hello', r["results"][0]['name']['first'], 'im from', r['results'][0]['location']['country'], 'my phone', r['results'][0]['phone'])