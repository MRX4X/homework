from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import *
driver = webdriver.Chrome()
driver.get("https://store.steampowered.com/?l=russian")
search_form = driver.find_element(by = "id", value="store_nav_search_term")
search_form.send_keys("стратегии")
search_form.send_keys(Keys.ENTER)
page_source = driver.page_source
with open('page_source.html', 'w', encoding='UTF-8') as f:
     f.write(page_source)
# buton_search = driver.find_element("store_search_link")
# buton_search.click()
with open('page_source.html', 'r', encoding='UTF-8') as f:
    page=f.read()
    bs=BeautifulSoup(page, 'lxml')
    conteiners_games = bs.find_all('span', "title")

    def artists():
        games_mas=[]

        for i in conteiners_games:
            games_mas.append(i.text)

        for j in games_mas:
             print(j)

    artists()