from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import *
import json

driver = webdriver.Chrome()
driver.maximize_window() # For maximizing window
driver.implicitly_wait(3) # gives an implicit wait for 20 seconds
driver.get("https://class.sirius.ru/authorize")

login_form = driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/div/div[1]/form/div[1]/div[1]/div/input")
driver.implicitly_wait(3)
login_form.send_keys("")
pass_form = driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/div/div[1]/form/div[1]/div[2]/div/input")
driver.implicitly_wait(3)
pass_form.send_keys("")
pass_form.send_keys(Keys.ENTER)

sheduled_form = driver.find_element(By.XPATH, "/html/body/div[1]/div/header/div/div/div/nav/div/a[4]/div[1]")
sheduled_form.click()

page_source = driver.page_source
# print(page_source)
with open('page_source.html', 'w', encoding='UTF-8') as f:
     f.write(page_source)

with open('page_source.html', 'r', encoding='UTF-8') as f:
    page=f.read()
    bs=BeautifulSoup(page, 'lxml')
    container = bs.find_all("div","schedule__day__content")
    result = {}
    for i in container:
        conteiners_day_week = i.find('p', "schedule__day__content__header__dayweek").text
        conteiners_lesson = i.find_all('span', "schedule-lesson")
        conteiners_lesson_room = i.find_all('div', "schedule__day__content__lesson__room")
        lessons = [x.text for x in conteiners_lesson]
        rooms = [x.text for x in conteiners_lesson_room]
        final = zip(lessons,[x.strip() for x in rooms ])
        result[conteiners_day_week] = list(final)
    print(result)


    # ELJUR_lesson_dictionary = dict(zip(lesson, lesson_room))
    # print(ELJUR_lesson_dictionary)
    # ELJUR_date_lesson_dictionary = dict(zip(day_week, ELJUR_lesson_dictionary))
    # print(ELJUR_date_lesson_dictionary)


with open('ELJIUR_sheduled.json', 'w',encoding="UTF-8") as write_file:
    json.dump(result,write_file,ensure_ascii=False,indent=4)
# driver.find_element_by_class_name('ваш атрибут name').click()
# sheduled_form = driver.find_element(By.XPATH, "/html/body/div[1]/div/header/div/div/div/nav/div/a[4]/div[1]")