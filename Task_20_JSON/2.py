import json

my_data={
    "name": "Denis",
    "age": "18",
    "countries": "RUSSIA"
}

my_dan=json.dumps(my_data)
with open('my.json', 'w') as write_file:
    write_file.write(my_dan)