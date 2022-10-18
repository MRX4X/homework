from functions_1 import *
s=input()
b=['Расп', 'расп', 'Стои', 'стои', 'Тел', 'тел', 'Кур', 'кур', 'Адр', 'адр']
if b[0] in s or b[1] in s:
    print(timetable())
if b[2] in s or b[3] in s:
    print(price())
if b[4] in s or b[5] in s:
    print(info())
if b[6] in s or b[7] in s:
    print(courses())
if b[8] in s or b[9] in s:
    print(adres())