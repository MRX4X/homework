from random import *
from time import *
class Game():
    def __init__(self, hp=100, k=200, mech=1, g=200, sol=1, p=1000):
        self.hp=hp
        self.k=k
        self.mech=mech
        self.g=g
        self.sol=sol
        self.p=p
    def Privet(self):
        print('Приветствуем в Игре "Трактир" 🏚. Тебе предстоит выполнить задания 🕵️️ и в конце получить монеты.\nСледуй инструкциям во время игры 🎮"')
        sleep(1)
    def Traktir(self):
        print("Ты находишься в Трактире 🏚. Перед тобой за стойкой трактирщик 🤵, а также другие посетители 🤠\nНужно выбрать к кому подойти:\nК трактирщику 🤵 - введи 1\nК посетителю 🤠 - введи 2")
        barmen_people=int(input())
        if barmen_people==1:
            print('Ты выбрал трактирщика 🤵, он тебе предлагает выпить 🍺. Нужно выбрать:\nДа - если выпьешь 🥃\nНет - если не желаешь 💪')
            barmen=input()
            if barmen=='да':
                print('Ты выбрал выпить 🥃, твое здоровье 🏥 уменьшилось')
                sleep(2)
                self.hp-=10
            if barmen=='нет':
                print('Ты не выбрал выпить 💪, поэтому держи задание.')
                sleep(2)
    def Kikimora(self):
        print('Твое задание - найти 🕵️️ артефакт ⚛️ кикиморы и принетси трактирщику')
        sleep(2)
        print('Ты вышел 🏃 из трактира 🏚 и идешь по лесу 🌲')
        sleep(2)
        print('Идешь ... 🏃')
        sleep(1)
        print('Идешь ... 🏃')
        sleep(1)
        print('Идешь ... 🏃')
        sleep(2)
        print('По дороге ты встретил Бабу-ягу 👵')
        sleep(2)
        print('От нее для тебя есть загадка 🔎 , разгадав которую, получишь подарок 🎁')
        sleep(2)
        print('🤔ЗАГАДКА🤔 - Вы заходите в тёмную кухню. В ней есть свеча, керосиновая лампа и газовая плита. Что вы зажжёте в первую очередь?')
        zagadka=input()
        if zagadka=='спичку':
            print('Ты ответил правильно ✅ , за это ты получашь меч 🗡')
            sleep(1)
        print('Идешь ... 🏃')
        sleep(1)
        print('Идешь ... 🏃')
        sleep(1)
        if zagadka == 'спичку':
            print('Ты дошел до кикиморы. Вы можете наносить удары 👊 , чтобы победить 🏆 . Она может вас топить в болоте и бить 👊 леанами. Будь осторожней ⚠️, удачи 🤞!')
            sleep(2)
            print('Введи - 1 для сражения 🤺')
            sleep(1)
            print('Введи 2 - для использования меча 🗡 ,который получил')
            mech=int(input())
            if mech==1:
                print('ХП 🏥 у вас', self.hp, 'ХП 🏥 у Кикиморы', self.k)
                sleep(1)
                print('Вы наносите удар 👊 первым')
                sleep(2)
                while True:
                    print('Выберите действие, указав число\n1)"удар 👊"\n2)"хил 🏥"')
                    hit = int(input())
                    if hit == 1:
                        b = randint(20, 60)
                        self.k -= b
                        print('У кикиморы осталось 🏥', self.k)
                        sleep(1)
                        print('Кикимора бьет 👊 леаной')
                        sleep(1)
                        c = randint(10, 30)
                        self.hp -= c
                        print('У вас осталось 🏥', self.hp)
                        sleep(1)
                    if hit == 2 and self.hp < 100:
                        if self.hp > 70:
                            self.hp += randint(10, 26)
                            print('Ваше хп 🏥', self.hp)
                        else:
                            self.hp += randint(10, 30)
                            print('Ваше хп 🏥', self.hp)
                    if self.hp <= 0:
                        print('Вы проиграли сражение и погибли ☠️')
                        break
                    if self.k <= 0:
                        print('Вы выйграли 🏆')
                        break
            if mech==2:
                print('Вы победили кикимору мечом 🗡, за это вы получили артефакт. С ним вы можете вернуться к трактирщику, и отдать его')
                self.mech-=1
        else:
            print(
                'Ты дошел до кикиморы. Вы можете наносить удары 👊, чтобы победить 🏆 ее. Она может вас топить в болоте и бить 👊 леанами. Будь осторожней ⚠️, удачи 🤞!')
            print('ХП у вас 🏥', self.hp, 'ХП у кикиморы 🏥', self.k)
            while True:
                print('Вы наносите удар 👊 первым')
                print('Выберите действие, указав число\n1)"удар 👊"\n2)"хил 🏥"')
                hit = int(input())
                if hit == 1:
                    b = randint(20, 60)
                    self.k -= b
                    print('У кикиморы осталось 🏥', self.k)
                    sleep(1)
                    print('Кикимора бьет 👊 леаной')
                    sleep(1)
                    c = randint(10, 30)
                    self.hp -= c
                    print('У вас осталось 🏥', self.hp)
                if hit == 2 and self.hp<100:
                    if self.hp>70:
                        self.hp+=randint(10, 26)
                        print('Ваше хп 🏥', self.hp)
                    else:
                        self.hp += randint(10, 30)
                        print('Ваше хп 🏥', self.hp)
                if self.hp <= 0:
                    print('Вы проиграли сражение и погибли ☠️')
                    break
                if self.k <= 0:
                    print('Вы выйграли 🏆')
                    break
        print('Возвращайтесь с артефактом ⚛️ к трактирщику.')
        print('Идешь ... 🏃')
        sleep(1)
        print('Идешь ... 🏃')
        sleep(1)
        print('Идешь ... 🏃')

    def Gargylia(self):
        print('Твое задание найти артефакт гаргулии и принетси бармену')
        print('Ты вышел из трактира и идешь по горам')
        print('Идешь ...')
        print(
            'Перед тобой появился Кащей-бесмертный, загадка Что не имеет длины, глубины, ширины, высоты, а можно измерить?')
        zagadka = input()
        if zagadka == 'Время' or zagadka == 'Температура':
            print('Ты ответил правильно, за это ты получашь соль')
        print('Идешь ...')
        if zagadka == 'Время' or zagadka == 'Температура' and self.mech==1:
            print(
                'Ты дошел до Гаргулии. Чтобы ее победить нужно сражаться - набери 1 или можешь возспользоваться мечом который получил - набери 2 или воспользоваться солью - набери 3 Вы можете наносить удары, чтобы победить ее. Она может вас преврать в камень. Будь осторожней, удачи!')
            mech = int(input())
            if mech == 1:
                print('ХП у вас', self.hp, 'ХП у Гаргулии', self.g)
                while True:
                    print('Вы наносите удар первым')
                    print('Выберите действие, указав число\n1)"удар"\n2)"хил"')
                    hit = int(input())
                    if hit == 1:
                        b = randint(20, 60)
                        self.g -= b
                        print('У Гаргулии осталось', self.g)
                        c = randint(10, 30)
                        self.hp -= c
                        print('У вас осталось', self.hp)
                    if hit == 2 and self.hp < 100:
                        if self.hp > 70:
                            self.hp += randint(10, 26)
                        else:
                            self.hp += randint(10, 30)
                            print('Ваше хп', self.hp)
                    if self.hp <= 0:
                        print('Вы проиграли')
                        break
                    if self.g <= 0:
                        print('Вы выйграли')
                        break
            if mech == 2:
                print(
                    'Вы победили Гаргулию мечом, за это вы получили артефакт. С ним вы можете вернуться к бармену и отдать его')
                self.mech-=1
            if mech == 3:
                print('Вы не можете победить гаргулью солью, но истратили ее и не сможете воспользоваться в будущем')
                self.sol-=1
                while True:
                    print('Вы наносите удар первым')
                    print('Выберите действие, указав число\n1)"удар"\n2)"хил"')
                    hit = int(input())
                    if hit == 1:
                        b = randint(20, 60)
                        self.g -= b
                        print('У Гаргулии осталось', self.g)
                        c = randint(10, 30)
                        self.hp -= c
                        print('У вас осталось', self.hp)
                    if hit == 2 and self.hp < 100:
                        if self.hp > 70:
                            self.hp += randint(10, 26)
                        else:
                            self.hp += randint(10, 30)
                            print('Ваше хп', self.hp)
                    if self.hp <= 0:
                        print('Вы проиграли')
                        break
                    if self.g <= 0:
                        print('Вы выйграли')
                        break
        else:
            print(
                'Ты дошел до Гаргулии. Вы можете наносить удары, чтобы победить ее. Она может вас преврать в камень. Будь осторожней, удачи!')
            print('ХП у вас', self.hp, 'ХП у Гаргулии', self.g)
            while True:
                print('Вы наносите удар первым')
                print('Выберите действие, указав число\n1)"удар"\n2)"хил"')
                hit = int(input())
                if hit == 1:
                    b = randint(20, 60)
                    self.g -= b
                    print('У Гаргулии осталось', self.g)
                    c = randint(10, 30)
                    self.hp -= c
                    print('У вас осталось', self.hp)
                if hit == 2 and self.hp < 100:
                    if self.hp > 70:
                        self.hp += randint(10, 26)
                    else:
                        self.hp += randint(10, 30)
                        print('Ваше хп', self.hp)
                if self.hp <= 0:
                    print('Вы проиграли')
                    break
                if self.g <= 0:
                    print('Вы выйграли')
                    break
        print('Вы возвращаетесь с артефактом к баремену')
        print('Идете...')
        print('Идете...')
        print('Идете...')
    def Prisrak(self):
        print('Твое задание найти артефакт гаргулии и принетси бармену')
        print('Ты вышел из трактира и идешь по горам')
        print('Идешь ...')
        print('Идешь ...')
        if self.mech==1 and self.sol==1:
            print(
                'Ты дошел до Призрака. Чтобы ее победить нужно сражаться - набери 1 или можешь возспользоваться мечом который получил - набери 2 или воспользоваться солью - набери 3 Вы можете наносить удары, чтобы победить ее. Она может вас преврать в камень. Будь осторожней, удачи!')
            mech = int(input())
            if mech == 1:
                print('ХП у вас', self.hp, 'ХП у Призрака', self.p)
                while True:
                    print('Вы наносите удар первым')
                    print('Выберите действие, указав число\n1)"удар"\n2)"хил"')
                    hit = int(input())
                    if hit == 1:
                        b = randint(20, 60)
                        self.g -= b
                        print('У Призрака осталось', self.g)
                        c = 100
                        self.hp -= c
                        print('У вас осталось', self.hp)
                    if hit == 2 and self.hp < 100:
                        if self.hp > 70:
                            self.hp += randint(10, 26)
                        else:
                            self.hp += randint(10, 30)
                            print('Ваше хп', self.hp)
                    if self.hp <= 0:
                        print('Вы проиграли. Для того, чтобы победить призрака нужно дополнительное оружие, которое вы получили при разгадывании загадок.')
                        break
                    if self.g <= 0:
                        print('Вы выйграли')
                        break
            if mech == 2:
                print('Вы проиграли. Нанесенного удара мечом не достаточно, чтобы победить Призрака.')
            if mech == 3:
                print('Вы победили Призрака солью')

        if self.mech==1:
            print(
                'Ты дошел до Призрака. Чтобы ее победить нужно сражаться - набери 1 или можешь возспользоваться мечом который получил - набери 2')
            mech = int(input())
            if mech == 1:
                print('ХП у вас', self.hp, 'ХП у Призрака', self.p)
                while True:
                    print('Вы наносите удар первым')
                    print('Выберите действие, указав число\n1)"удар"\n2)"хил"')
                    hit = int(input())
                    if hit == 1:
                        b = randint(20, 60)
                        self.g -= b
                        print('У Призрака осталось', self.g)
                        c = 100
                        self.hp -= c
                        print('У вас осталось', self.hp)
                    if hit == 2 and self.hp < 100:
                        if self.hp > 70:
                            self.hp += randint(10, 26)
                        else:
                            self.hp += randint(10, 30)
                            print('Ваше хп', self.hp)
                    if self.hp <= 0:
                        print('Вы проиграли. Для того, чтобы победить призрака нужно дополнительное оружие, которое вы получили при разгадывании загадок.')
                        break
                    if self.g <= 0:
                        print('Вы выйграли')
                        break
            if mech == 2:
                print('Вы проиграли. Нанесенного удара мечом не достаточно, чтобы победить Призрака.')
        if self.sol==1:
            print(
                'Ты дошел до Призрака. Чтобы ее победить нужно сражаться - набери 1 или можешь возспользоваться солью - набери 2')
            mech = int(input())
            if mech == 1:
                print('ХП у вас', self.hp, 'ХП у Призрака', self.p)
                while True:
                    print('Вы наносите удар первым')
                    print('Выберите действие, указав число\n1)"удар"\n2)"хил"')
                    hit = int(input())
                    if hit == 1:
                        b = randint(20, 60)
                        self.g -= b
                        print('У Призрака осталось', self.g)
                        c = 100
                        self.hp -= c
                        print('У вас осталось', self.hp)
                    if hit == 2 and self.hp < 100:
                        if self.hp > 70:
                            self.hp += randint(10, 26)
                        else:
                            self.hp += randint(10, 30)
                            print('Ваше хп', self.hp)
                    if self.hp <= 0:
                        print('Вы проиграли. Для того, чтобы победить призрака нужно дополнительное оружие, которое вы получили при разгадывании загадок.')
                        break
                    if self.g <= 0:
                        print('Вы выйграли')
                        break
            if mech == 2:
                print('Вы пробедили')
        else:
            print('ХП у вас', self.hp, 'ХП у Призрака', self.p)
            while True:
                print('Вы наносите удар первым')
                print('Выберите действие, указав число\n1)"удар"\n2)"хил"')
                hit = int(input())
                if hit == 1:
                    b = randint(20, 60)
                    self.g -= b
                    print('У Призрака осталось', self.g)
                    c = 100
                    self.hp -= c
                    print('У вас осталось', self.hp)
                if hit == 2 and self.hp < 100:
                    if self.hp > 70:
                        self.hp += randint(10, 26)
                    else:
                        self.hp += randint(10, 30)
                        print('Ваше хп', self.hp)
                if self.hp <= 0:
                    print(
                        'Вы проиграли. Для того, чтобы победить призрака нужно дополнительное оружие, которое вы получили при разгадывании загадок.')
                    break
                if self.g <= 0:
                    print('Вы выйграли')
                    break
        print('Вы возвращаетесь с артефактом к баремену')
        print('Идете...')
        print('Идете...')
        print('Идете...')

c1=Game()
c1.Privet()
c1.Traktir()
c1.Kikimora()
c1.Traktir()
c1.Gargylia()
c1.Traktir()
c1.Prisrak()


