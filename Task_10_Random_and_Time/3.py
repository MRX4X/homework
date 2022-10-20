from random import randint
a=int(input('Введите общее число участников'))
while a!=0:
    b=randint(1, a)
    print('Ваш номер', b)
    c=randint(1, a)
    d=a-c
    print('Участников в первом забеге', d, 'Участников во втором забеге', c)
    break