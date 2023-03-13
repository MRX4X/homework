import requests
from bs4 import BeautifulSoup
import requests

#
# cookies = {
#     'stest201': '0',
#     'stest207': 'acc0',
#     'stest209': 'ct1',
#     'tp_city_id': '38733',
#     'PHPSESSID': '1c81e28afa82075d2bb24e79d18657c1',
#     'user_public_id': '7%2Fo%2B0iBf%2BNxW4jMY2o%2BsYgPPkP5%2FcWxP2%2B2WaS%2BvywYkbEzExB34zgpVvA2%2Fewew',
#     '_gcl_au': '1.1.1237103271.1678192025',
#     '_gid': 'GA1.2.343699606.1678192027',
#     '_ym_uid': '1678192027247311240',
#     '_ym_d': '1678192027',
#     'tmr_lvid': '574c54b04bf1eb72ad528c92e455c892',
#     'tmr_lvidTS': '1678192026897',
#     '_ym_isad': '2',
#     '_ym_visorc': 'b',
#     'adrdel': '1',
#     'adrcid': 'AzxWcdNnEK3N93dgZwf0ONw',
#     'afUserId': 'a693d850-a6e6-4d41-b2af-811ce795f4e1-p',
#     'AF_SYNC': '1678192028253',
#     '_userGUID': '0:ley87es9:VuQCiLj5tNUVYg2k8EMQk6~iRt1vpQwZ',
#     'c2d_widget_id': '{%229eb3fbdda817d48faffc65c3446228e8%22:%22[chat]%20f99f3da4132e549bef2e%22}',
#     'game3dTopperClosed': 'true',
#     'promo1000closed': 'true',
#     'pageviewTimerFired15': 'true',
#     'pageviewTimerFired30': 'true',
#     'pageviewTimerFired60': 'true',
#     'mindboxDeviceUUID': 'c7913a47-c3d6-4c31-883f-ab93c1d97df2',
#     'directCrm-session': '%7B%22deviceGuid%22%3A%22c7913a47-c3d6-4c31-883f-ab93c1d97df2%22%7D',
#     'tmr_detect': '0%7C1678194970501',
#     '_gat_UA-25136986-1': '1',
#     'qrator_jsid': '1678192022.611.Hb7DZ4w9afvMdyFb-vvtsjrp38vcduh2esfhqdjsdt50dbehk',
#     'visitedPagesNumber': '7',
#     '_ga_RD4H4CBNJ3': 'GS1.1.1678192025.1.1.1678195123.55.0.0',
#     '_ga': 'GA1.1.1993479249.1678192026',
#     'pageviewTimer': '3087.4169999999995',
# }
#
# headers = {
#     'authority': 'sochi.technopark.ru',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
#     # 'cookie': 'stest201=0; stest207=acc0; stest209=ct1; tp_city_id=38733; PHPSESSID=1c81e28afa82075d2bb24e79d18657c1; user_public_id=7%2Fo%2B0iBf%2BNxW4jMY2o%2BsYgPPkP5%2FcWxP2%2B2WaS%2BvywYkbEzExB34zgpVvA2%2Fewew; _gcl_au=1.1.1237103271.1678192025; _gid=GA1.2.343699606.1678192027; _ym_uid=1678192027247311240; _ym_d=1678192027; tmr_lvid=574c54b04bf1eb72ad528c92e455c892; tmr_lvidTS=1678192026897; _ym_isad=2; _ym_visorc=b; adrdel=1; adrcid=AzxWcdNnEK3N93dgZwf0ONw; afUserId=a693d850-a6e6-4d41-b2af-811ce795f4e1-p; AF_SYNC=1678192028253; _userGUID=0:ley87es9:VuQCiLj5tNUVYg2k8EMQk6~iRt1vpQwZ; c2d_widget_id={%229eb3fbdda817d48faffc65c3446228e8%22:%22[chat]%20f99f3da4132e549bef2e%22}; game3dTopperClosed=true; promo1000closed=true; pageviewTimerFired15=true; pageviewTimerFired30=true; pageviewTimerFired60=true; mindboxDeviceUUID=c7913a47-c3d6-4c31-883f-ab93c1d97df2; directCrm-session=%7B%22deviceGuid%22%3A%22c7913a47-c3d6-4c31-883f-ab93c1d97df2%22%7D; tmr_detect=0%7C1678194970501; _gat_UA-25136986-1=1; qrator_jsid=1678192022.611.Hb7DZ4w9afvMdyFb-vvtsjrp38vcduh2esfhqdjsdt50dbehk; visitedPagesNumber=7; _ga_RD4H4CBNJ3=GS1.1.1678192025.1.1.1678195123.55.0.0; _ga=GA1.1.1993479249.1678192026; pageviewTimer=3087.4169999999995',
#     'if-none-match': '"14508f-e5e2K89brbEhf0okfv04eEbg+L8"',
#     'referer': 'https://sochi.technopark.ru/smartfony-i-gadzhety/',
#     'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"macOS"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
# }
#
# response = requests.get('https://sochi.technopark.ru/smartfony/', cookies=cookies, headers=headers)
# print(response)
# # print(response.text)
# with open('page.html', 'w', encoding="UTF-8") as f:
#     f.write(response.text)

with open('page.html', 'r', encoding="UTF-8") as file:
    page=file.read()
    bs=BeautifulSoup(page, 'lxml')
    conteiners=bs.find_all('div',"product-card-big__container")
    result={}
    for i in conteiners:
        name=i.find('div', 'product-card-big__name').text[13:-11]
        price = i.find('div', 'product-prices__price').text[5:-5]
        result[name]=price
    print(result)
