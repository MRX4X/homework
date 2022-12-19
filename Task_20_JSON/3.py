import json
import weakref

my_data={
    "name": 'Denis',
    "age": 18,
    "countries": [{
        "name": "Rissia",
        "time": "12",
        "cities": "Saint-Peterburg, Moscow, Sochi"
    }]
}

my_dan=json.dumps(my_data)
with open('my.json', 'w') as f:
    f.write(my_dan)