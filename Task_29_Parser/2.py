import requests
from bs4 import *
import json
# url='https://music.yandex.ru/chart'
# response=requests.get(url)
# with open('charts.html', 'w', encoding='UTF-8') as f:
#     f.write(response.text)

with open('charts.html', 'r', encoding='UTF-8') as f:
    page=f.read()
    bs=BeautifulSoup(page, 'lxml')
    conteiners_artist = bs.find_all('span', "d-track__artists")
    conteiners_music = bs.find_all('div', "d-track__name")

    def artists():
        artists_mas=[]

        for i in conteiners_artist:
            artists_mas.append(i.text)

        return artists_mas
    charts_artists=artists()


    def music():
        music_mas=[]

        for j in conteiners_music:
            music_mas.append(j.text)

        return music_mas
    charts_music=music()

    # l3 = [' :'.join(x) for x in zip(charts_artists, charts_music)]
    # print(l3)
    music_dictionary = dict(zip(charts_artists, charts_music))



my_file_json=json.dumps(music_dictionary)
with open('charts_data.json', 'w') as write_file:
    write_file.write(my_file_json)