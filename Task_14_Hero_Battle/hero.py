from time import *
from random import *
class Game():
    def privet(self):
        return ('Привет в игре Игра престолов')
    def Location(self):
        print('Выбери одну из 3 возможных локаций: Красная поляна, Солнечная долина, Роза хутор')
        loc=input()
        if loc=='Красная поляна':
            return ('Ты выбрал локацию Красная Поляна')
        if loc=='Солнечная долина':
            return ('Ты выбрал локацию Солнечная долина')
        if loc=='Роза хутор':
            return ('Ты выбрал локацию Роза хутор')
        else:
            return ('Такой локации пока нет в игре')
    def Time(self):
        return ('Вы идете по карте....')

class Fight_1():
    def razboi(self):
        global mon
        mon = 100
        print('Вы встретили перед собой разбойников\nОни требуют откуп в размере 50 монет, у вас есть', mon, 'монет, иначе вам придется сражаться\nВыбирайте: ОТКУП или СРАЖЕНИЕ')
        raz=input()
        if raz=='Откуп':
            raz_ploh=mon/2
            print('Вы откупились, но ваше количество монет стало', raz_ploh)
        if raz=='Сражение':
            print(
                'Вы выбрали сражение. Из средств обороны у вас есть только кулаки.\nВыберите действие, указав число\n1)"удар"\n2)"хил"')
            vi = 100
            raz_1 = 100
            print('У вас hp -', vi, 'У разбойника -', raz_1)
            while True:
                hit = int(input())
                if hit == 1:
                    b = randint(20, 60)
                    raz_1 -= b
                    print('У разбойника осталось', raz_1)
                    c = randint(1, 4)
                    vi -= c
                    print('У вас осталось', vi)
                if hit == 2:
                    vi += randint(10, 30)
                    print('Ваше хп', vi)
                if vi <= 0:
                    print('Вы проиграли')
                    break
                if raz_1 <= 0:
                    print('Вы выйграли')
                    break
f1=Game()
print(f1.privet())
print(f1.Location())
print(f1.Time())

sleep(2)

f2=Fight_1()
print(f2.razboi())

