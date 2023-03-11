import requests
def random_cats_pictures():
    for i in range(2):
        my_file = open(f'Кот_рандомный{i}', 'wb')
        my_file.write(requests.get('https://cataas.com/cat').content)

def random_cats_pictures_origin():
    for i in range(2):
        my_file = open(f'Кот_оригинальный{i}', 'wb')
        my_file.write(requests.get('https://cataas.com/cat?type=original').content)

def random_cats_pictures_pixel():
    for i in range(2):
        my_file = open(f'Кот_пиксельный{i}', 'wb')
        my_file.write(requests.get('https://cataas.com/cat?filter=pixel').content)

random_cats_pictures()
random_cats_pictures_origin()
random_cats_pictures_pixel()