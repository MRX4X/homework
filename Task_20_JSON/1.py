import json
with open('character.json', 'r') as write_file:
    data= json.load(write_file)
print(data["name"])
print(data["origin"]["name"])
print(data["episode"])