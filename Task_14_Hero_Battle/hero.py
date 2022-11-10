from time import *
from random import *
class Game():
    def privet(self):
        return ('Привет! Ты зашел в игру "Бродилка". Следуй инструкциям во время игры.')
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
        mon=100
        print('Вы встретили перед собой разбойника')
        sleep(1)
        print('Он требует откуп в размере 50 монет, у вас есть', mon, 'монет, иначе вам придется сражаться')
        sleep(1)
        print('Выбирайте: ОТКУП или СРАЖЕНИЕ')
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
                    b = randint(20, 40)
                    raz_1 -= b
                    print('У разбойника осталось', raz_1)
                    c = randint(20, 40)
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

class Fight_2():
    def razboi_1(self):
        print('Вы встретили другого пользователя.\nВступите с ним в бой.')
        sleep(1)
        vi = 100
        prot = 100
        print('У вас hp -', vi, 'У соперника -', prot)
        sleep(1)
        print('Выберите 1 для удара ИЛИ 2 для хила')
        count_1=0
        count_2=0
        while True:
            #первый игрок
            print('Аттакует 1 игрок')
            print('ХП 1 игрока ', vi)
            hit_1 = int(input())
            if hit_1 == 1:
                b = randint(20, 40)
                prot -= b
                print('У врага', prot)
            if count_1<=3:
                if hit_1 == 2:
                    vi += randint(10, 30)
                    print('Ваше хп', vi)
                    count_1+=1
            else:
                print('Максимальное количество хилок - 3')
            #второй игрок
            print('Аттакует 2 игрок')
            print('ХП 2 игрока ', prot)
            hit_2 = int(input())
            if hit_2 == 1:
                b = randint(20, 40)
                vi -= b
                print('У врага', vi)
            if count_2<=3:
                if hit_2 == 2:
                    prot += randint(10, 30)
                    print('Ваше хп', prot)
                    count_2+=1
            else:
                print('Максимальное количество хилок - 3')
            if vi <= 0:
                print('1 игрок проиграл')
                sleep(1)
                print('Поздравляем!!! Вы победили всех врагов и прошли игру')
                break
            if prot <= 0:
                print('2 игрок проиграл')
                sleep(1)
                print('Вы погибли')
                break

class Day():
    def Sleep(self):
        print('День подходит к концу\nВашему герою нужен обязательный сон')
        sleep(1)
        print('Спит.....')
        sleep(1)
        print('Спит....')
        sleep(1)
        print('Доброе утро! Начало новых приключений!')
        sleep(1)
        print('Новый день!')

f1=Game()
print(f1.privet())
print(f1.Location())
print(f1.Time())

sleep(2)

f2=Fight_1()
f2.razboi()

sleep(2)

f3=Day()
f3.Sleep()

sleep(2)

f4=Fight_2()
f4.razboi_1()
