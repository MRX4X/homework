import requests
r=requests.get('https://randomuser.me/api/').text
print(r)
# print(f'Hi, im {r[]}, im from #COUNTRY, my phone number is #PHONE')