from time import *
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
        sleep(5)
class Fight_1():
    def money(self):
        global mon
        mon=100
    def razboi(self):
        return ('Вы встретили перед собой разбойников\nОни требуют откуп в размере 50 монет, у вас есть', mon, 'монет, иначе вам придется сражаться\nВыбирайте: ОТКУП или СРАЖЕНИЕ')
        raz=input()
        if raz=='Откуп':
            raz_ploh=mon/2
            return ('Вы откупились, но ваше количество монет стало', raz_ploh)
        if raz=='Сражение':
            s='Вызвать файл с файтом'
f1=Game()
print(f1.privet())
print(f1.Location())
print(f1.Time())

