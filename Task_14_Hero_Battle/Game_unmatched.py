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
        print('Приветствуем в Игре "Трактир" 🏚. Тебе предстоит выполнить задания 🕵️️ и в конце получить монеты.')
        sleep(1)
        print('Следуй инструкциям во время игры 🎮')
        sleep(1)
    def Traktir(self):
        print("Ты находишься в Трактире 🏚. Перед тобой за стойкой трактирщик 🤵, а также другие посетители 🤠")
        sleep(1)
        print('Нужно выбрать к кому подойти:')
        sleep(1)
        print('К трактирщику 🤵 - введи 1')
        sleep(1)
        print('К посетителю 🤠 - введи 2')
        barmen_people=int(input())
        if barmen_people==1:
            print('Ты выбрал трактирщика 🤵, он тебе предлагает выпить 🍺.')
            sleep(1)
            print('Нужно выбрать:')
            sleep(1)
            print('Да - если выпьешь 🥃')
            sleep(1)
            print('Нет - если не желаешь 💪')
            barmen=input()
            if barmen=='да':
                print('Ты выбрал выпить 🥃, твое здоровье 🏥 уменьшилось на 10 единиц')
                sleep(2)
                print('Трактирщик🤵 дал тебе задание 🕵️')
                self.hp-=10
            if barmen=='нет':
                print('Ты не выбрал выпить 💪, поэтому держи задание.')
                sleep(2)
        if barmen_people==2:
            print('- Ну здравствствуй, ДЖО.')
            sleep(1)
            print('- Ты хотел нас обмануть на 5 золоченных? ААААА?!')
            print('Завязалась драка')
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
                        sleep(1)
                    else:
                        self.hp += randint(10, 30)
                        print('Ваше хп 🏥', self.hp)
                        sleep(1)
                if self.hp <= 0:
                    print('Вы проиграли сражение и погибли ☠️')
                    break
                if self.k <= 0:
                    print('Вы выйграли 🏆')
                    break
    def Kikimora(self):
        print('Твое задание - найти 🕵️️ артефакт ⚛️ Кикиморы и принетси трактирщику 🤵')
        sleep(3)
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
        else:
            print('Ты ответил не верно ❌, поэтому не получаешь подарок')
            self.mech-=1
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
            count_Kikimora_1=0
            mech=int(input())
            if mech==1:
                print('Ты выбрал сражение 🤺')
                sleep(1)
                print('ХП 🏥 у вас', self.hp, ' ХП 🏥 у Кикиморы', self.k)
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
                    if hit == 2 and self.hp < 100 and count_Kikimora_1<=4:
                        if self.hp > 70:
                            self.hp += randint(10, 26)
                            print('Ваше хп 🏥', self.hp)
                            count_Kikimora_1+=1
                            sleep(1)
                        else:
                            self.hp += randint(10, 30)
                            print('Ваше хп 🏥', self.hp)
                            count_Kikimora_1+=1
                            sleep(1)
                    if self.hp <= 0:
                        print('Вы проиграли сражение и погибли ☠️')
                        break
                    if self.k <= 0:
                        print('Вы выйграли 🏆')
                        break
            if mech==2:
                print('Вы победили кикимору мечом 🗡, за это вы получили артефакт ⚛️. С ним вы можете вернуться к трактирщику, и отдать его')
                self.mech-=1
        else:
            print('Ты дошел до кикиморы. Вы можете наносить удары 👊, чтобы победить 🏆 .')
            sleep(2)
            print('Она может вас топить в болоте и бить 👊 леанами. Будь осторожней ⚠️, удачи 🤞!')
            sleep(2)
            print('ХП у вас 🏥', self.hp, 'ХП у кикиморы 🏥', self.k)
            sleep(2)
            print('Вы наносите удар 👊 первым')
            count_Kikimora_2=0
            while True:
                print('Выберите действие, указав число\n1)"удар 👊"\n2)"хил 🏥"')
                hit = int(input())
                if hit == 1:
                    b = randint(20, 60)
                    self.k -= b
                    print('У Кикиморы осталось 🏥', self.k)
                    sleep(1)
                    print('Кикимора бьет 👊 леаной')
                    sleep(1)
                    c = randint(10, 30)
                    self.hp -= c
                    print('У вас осталось 🏥', self.hp)
                    sleep(2)
                if hit == 2 and self.hp<100:
                    if self.hp>70:
                        self.hp+=randint(10, 26)
                        print('Ваше хп 🏥', self.hp)
                        count_Kikimora_2+=1
                        sleep(1)
                    else:
                        self.hp += randint(10, 30)
                        print('Ваше хп 🏥', self.hp)
                        count_Kikimora_2+=1
                        sleep(1)
                if self.hp <= 0:
                    print('Вы проиграли сражение и погибли ☠️')
                    break
                if self.k <= 0:
                    print('Вы выйграли 🏆')
                    break
        print('Возвращайтесь с артефактом ⚛️ к трактирщику 🤵')
        print('Идешь ... 🏃')
        sleep(1)
        print('Идешь ... 🏃')
        sleep(1)
        print('Идешь ... 🏃')

    def Gargylia(self):
        print('Твое задание 🕵️ найти артефакт ⚛️ Гаргулии и принетси трактирщику')
        sleep(2)
        print('Ты вышел 🏃 из трактира 🏚 и идешь по лесу 🏔')
        sleep(2)
        print('Идешь ... 🏃')
        sleep(1)
        print('Идешь ... 🏃')
        sleep(1)
        print('Идешь ... 🏃')
        sleep(2)
        print('По дороге ты встретил Кащея-бесмертного ☠️')
        sleep(2)
        print('От него для тебя есть загадка 🔎 , разгадав которую, получишь подарок 🎁')
        sleep(2)
        print(
            '🤔ЗАГАДКА🤔 - Что не имеет длины, глубины, ширины, высоты, а можно измерить?')
        zagadka = input()
        if zagadka == 'время' or zagadka == 'температура':
            print('Ты ответил правильно ✅ , за это ты получашь ядовитый гриб 🍄')
            sleep(1)
        else:
            print('Ты ответил не верно ❌, поэтому не получаешь подарок')
            self.sol-=1
            sleep(1)
        print('Идешь ... 🏃')
        sleep(1)
        print('Идешь ... 🏃')
        sleep(1)
        if zagadka == 'время' or zagadka == 'температура' and self.mech==1:
            print(
                'Ты дошел до Гаргулии. Вы можете наносить удары 👊 , чтобы победить 🏆 .Она может вас преврать в камень. Будь осторожней ⚠️, удачи 🤞!')
            sleep(2)
            print('Введи - 1 для сражения 🤺')
            sleep(1)
            print('Введи 2 - для использования меча 🗡 ,который получил')
            sleep(1)
            print('Введи - 3 для использования ядовитым грибом 🍄')
            mech = int(input())
            if mech == 1:
                print('Ты выбрал сражение 🤺')
                sleep(1)
                print('ХП 🏥 у вас', self.hp, 'ХП 🏥 у Гаргулии', self.k)
                sleep(1)
                print('Вы наносите удар 👊 первым')
                sleep(2)
                while True:
                    print('Выберите действие, указав число\n1)"удар 👊"\n2)"хил 🏥"')
                    hit = int(input())
                    if hit == 1:
                        b = randint(20, 60)
                        self.g -= b
                        print('У Гаргулии осталось 🏥', self.g)
                        sleep(1)
                        print('Гаргулия кидает 👊 камень')
                        sleep(1)
                        c = randint(10, 30)
                        self.hp -= c
                        print('У вас осталось 🏥', self.hp)
                        sleep(1)
                    if hit == 2 and self.hp < 100:
                        if self.hp > 70:
                            self.hp += randint(10, 26)
                            print('Ваше хп 🏥', self.hp)
                            sleep(1)
                        else:
                            self.hp += randint(10, 30)
                            print('Ваше хп 🏥', self.hp)
                            sleep(1)
                    if self.hp <= 0:
                        print('Вы проиграли сражение и погибли ☠️')
                        break
                    if self.g <= 0:
                        print('Вы выйграли 🏆')
                        break
            if mech == 2:
                print('Вы победили Гаргулию мечом 🗡, за это вы получили артефакт ⚛️ . С ним вы можете вернуться к трактирщику 🤵, и отдать его')
                self.mech-=1
            if mech == 3:
                print('Вы не можете победить Гаргулью ядовитыйм грибом 🍄, но истратили ее и не сможете воспользоваться в будущем')
                sleep(1)
                self.sol-=1
                print('Вы наносите удар 👊 первым')
                sleep(1)
                while True:
                    print('Выберите действие, указав число\n1)"удар 👊"\n2)"хил 🏥"')
                    hit = int(input())
                    if hit == 1:
                        b = randint(20, 60)
                        self.g -= b
                        print('У Гаргулии осталось 🏥', self.g)
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
                            sleep(1)
                        else:
                            self.hp += randint(10, 30)
                            print('Ваше хп 🏥', self.hp)
                            sleep(1)
                    if self.hp <= 0:
                        print('Вы проиграли сражение и погибли ☠️')
                        break
                    if self.k <= 0:
                        print('Вы выйграли 🏆')
                        break
        else:
            print('Ты дошел до Гаргулии. Вы можете наносить удары 👊, чтобы победить 🏆 .')
            sleep(2)
            print('Она может в вас кидать камнями 👊 . Будь осторожней ⚠️, удачи 🤞!')
            sleep(2)
            print('ХП у вас 🏥', self.hp, 'ХП у кикиморы 🏥', self.k)
            sleep(2)
            print('Вы наносите удар 👊 первым')
            sleep(1)
            while True:
                print('Выберите действие, указав число\n1)"удар 👊"\n2)"хил 🏥"')
                hit = int(input())
                if hit == 1:
                    b = randint(20, 60)
                    self.g -= b
                    print('У Гаргулии осталось 🏥', self.g)
                    sleep(1)
                    print('Гаргулия кидает 👊 камень')
                    sleep(1)
                    c = randint(10, 30)
                    self.hp -= c
                    print('У вас осталось 🏥', self.hp)
                    sleep(2)
                if hit == 2 and self.hp<100:
                    if self.hp>70:
                        self.hp+=randint(10, 26)
                        print('Ваше хп 🏥', self.hp)
                        sleep(1)
                    else:
                        self.hp += randint(10, 30)
                        print('Ваше хп 🏥', self.hp)
                        sleep(1)
                if self.hp <= 0:
                    print('Вы проиграли сражение и погибли ☠️')
                    break
                if self.k <= 0:
                    print('Вы выйграли 🏆')
                    break
        print('Возвращайтесь с артефактом ⚛️ к трактирщику 🤵')
        print('Идешь ... 🏃')
        sleep(1)
        print('Идешь ... 🏃')
        sleep(1)
        print('Идешь ... 🏃')
    def Prisrak(self):
        print('Твое задание 🕵️ найти артефакт ⚛️ Призрака и принетси трактирщику')
        sleep(2)
        print('Ты вышел 🏃 из трактира 🏚 и идешь по лесу 🏔')
        sleep(2)
        print('Идешь ... 🏃')
        sleep(1)
        print('Идешь ... 🏃')
        sleep(1)
        print('Идешь ... 🏃')
        sleep(2)
        if self.mech==1 and self.sol==1:
            print(
                'Ты дошел до Призрака. Вы можете наносить удары 👊 , чтобы победить 🏆 . Он может наносить вам урон 👊 . Будь осторожней ⚠️, удачи 🤞!')
            sleep(2)
            print('Введи - 1 для сражения 🤺')
            sleep(1)
            print('Введи 2 - для использования меча 🗡 ,который получил')
            sleep(1)
            print('Введи 3 - для использование ядовитого гриба 🍄')
            mech = int(input())
            if mech == 1:
                print('Ты выбрал сражение 🤺')
                sleep(1)
                print('ХП 🏥 у вас', self.hp, ' ХП 🏥 у Кикиморы', self.k)
                sleep(1)
                print('Вы наносите удар 👊 первым')
                sleep(2)
                while True:
                    print('Выберите действие, указав число\n1)"удар 👊"\n2)"хил 🏥"')
                    hit = int(input())
                    if hit == 1:
                        b = randint(20, 60)
                        self.g -= b
                        print('У Призрака осталось 🏥', self.g)
                        c = 100
                        sleep(1)
                        print('Призрак наносит 👊 удар')
                        sleep(1)
                        self.hp -= c
                        print('У вас осталось 🏥', self.hp)
                    if hit == 2 and self.hp < 100:
                        if self.hp > 70:
                            self.hp += randint(10, 26)
                            print('Ваше хп 🏥', self.hp)
                        else:
                            self.hp += randint(10, 30)
                            print('Ваше хп 🏥', self.hp)
                    if self.hp <= 0:
                        print('Вы проиграли сражение и погибли ☠️ . Для того, чтобы победить призрака нужно дополнительное оружие, которое вы получили при разгадывании загадок.')
                        break
                    if self.g <= 0:
                        print('Вы выйграли 🏆')
                        break
            if mech == 2:
                print('Вы проиграли сражение и погибли ☠️ . Нанесенного удара мечом 🗡 не достаточно, чтобы победить Призрака.')
            if mech == 3:
                print('Вы победили Призрака ядовитым грибом 🍄')

        if self.mech==1:
            print(
                'Ты дошел до Призрака. Вы можете наносить удары 👊 , чтобы победить 🏆 . Он может наносить вам урон 👊 . Будь осторожней ⚠️, удачи 🤞!')
            mech = int(input())
            if mech == 1:
                print('Ты выбрал сражение 🤺')
                sleep(1)
                print('ХП 🏥 у вас', self.hp, ' ХП 🏥 у Призрака', self.k)
                sleep(1)
                print('Вы наносите удар 👊 первым')
                sleep(2)
                while True:
                    print('Выберите действие, указав число\n1)"удар 👊"\n2)"хил 🏥"')
                    hit = int(input())
                    if hit == 1:
                        b = randint(20, 60)
                        self.g -= b
                        print('У Призрака осталось 🏥', self.g)
                        c = 100
                        sleep(1)
                        print('Призрак наносит 👊 удар')
                        sleep(1)
                        self.hp -= c
                        print('У вас осталось 🏥', self.hp)
                    if hit == 2 and self.hp < 100:
                        if self.hp > 70:
                            self.hp += randint(10, 26)
                            print('Ваше хп 🏥', self.hp)
                        else:
                            self.hp += randint(10, 30)
                            print('Ваше хп', self.hp)
                    if self.hp <= 0:
                        print(
                            'Вы проиграли сражение и погибли ☠️ . Для того, чтобы победить призрака нужно дополнительное оружие, которое вы получили при разгадывании загадок.')
                        break
                    if self.g <= 0:
                        print('Вы выйграли 🏆')
                        break
            if mech == 2:
                print(
                    'Вы проиграли сражение и погибли ☠️ . Нанесенного удара мечом 🗡 не достаточно, чтобы победить Призрака.')
        if self.sol==1:
            print(
                'Ты дошел до Призрака. Чтобы ее победить нужно сражаться - набери 1 или можешь возспользоваться ядовитым грибом 🍄 - набери 2')
            mech = int(input())
            if mech == 1:
                print('Ты выбрал сражение 🤺')
                sleep(1)
                print('ХП 🏥 у вас', self.hp, ' ХП 🏥 у Призрака', self.k)
                sleep(1)
                print('Вы наносите удар 👊 первым')
                sleep(2)
                while True:
                    print('Выберите действие, указав число\n1)"удар 👊"\n2)"хил 🏥"')
                    hit = int(input())
                    if hit == 1:
                        b = randint(20, 60)
                        self.g -= b
                        print('У Призрака осталось 🏥', self.g)
                        c = 100
                        sleep(1)
                        print('Призрак наносит 👊 удар')
                        sleep(1)
                        self.hp -= c
                        print('У вас осталось 🏥', self.hp)
                    if hit == 2 and self.hp < 100:
                        if self.hp > 70:
                            self.hp += randint(10, 26)
                            print('Ваше хп 🏥', self.hp)
                        else:
                            self.hp += randint(10, 30)
                            print('Ваше хп 🏥', self.hp)
                    if self.hp <= 0:
                        print('Вы проиграли сражение и погибли ☠️ . Для того, чтобы победить призрака нужно дополнительное оружие, которое вы получили при разгадывании загадок.')
                        break
                    if self.g <= 0:
                        print('Вы выйграли 🏆')
                        break
            if mech == 2:
                print('Вы пробедили 🏆')
        else:
            print('ХП 🏥 у вас', self.hp, ' ХП 🏥 у Призрака', self.k)
            sleep(1)
            print('Вы наносите удар 👊 первым')
            sleep(2)
            while True:
                print('Выберите действие, указав число\n1)"удар 👊"\n2)"хил 🏥"')
                hit = int(input())
                if hit == 1:
                    b = randint(20, 60)
                    self.g -= b
                    print('У Призрака осталось 🏥', self.g)
                    c = 100
                    sleep(1)
                    print('Призрак наносит 👊 удар')
                    sleep(1)
                    self.hp -= c
                    print('У вас осталось 🏥', self.hp)
                if hit == 2 and self.hp < 100:
                    if self.hp > 70:
                        self.hp += randint(10, 26)
                        print('Ваше хп 🏥', self.hp)
                    else:
                        self.hp += randint(10, 30)
                        print('Ваше хп 🏥', self.hp)
                if self.hp <= 0:
                    print('Вы проиграли сражение и погибли ☠️ . Для того, чтобы победить призрака нужно дополнительное оружие, которое вы получили при разгадывании загадок.')
                    break
                if self.g <= 0:
                    print('Вы выйграли 🏆')
                    break
            if mech == 2:
                print('Вы пробедили 🏆')
        print('Возвращайтесь с артефактом ⚛️ к трактирщику 🤵')
        print('Идешь ... 🏃')
        sleep(1)
        print('Идешь ... 🏃')
        sleep(1)
        print('Идешь ... 🏃')
    def The_end(self):
        print('Ты прошел через всех врагов')
        sleep(1)
        print('Принес все артефакты')
        sleep(1)
        print('Трактирщик тебе благодарен и уже делает отборную выпивку')
        sleep(1)
        print('- Держи выпивки, ты заслужил!')
        sleep(1)
        print('После создания выпивки, трактир прославился и вы получаете столько денег, что хватит до конца жизни')
        sleep(1)
        print('На этом игра заканчивается. Хорошего дня!')
c1=Game()
c1.Privet()
c1.Traktir()
c1.Kikimora()
c1.Traktir()
c1.Gargylia()
c1.Traktir()
c1.Prisrak()


