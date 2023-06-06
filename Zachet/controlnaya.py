from time import *
from datetime import datetime
class Post():
    def __init__(self, nikname, time, like, rug, kom_mas=''):
        self.nikname = nikname
        self.time = time
        self.like = like
        self.rug = rug
        self.kom_mas = kom_mas
    def User_like(self):
        print('VK....')
        sleep(1)
        print('VK....')
        sleep(1)
        print(self.nikname, 'Вы вошли в Vk', 'Время', datetime.now())
        sleep(1)
        print('Ваш друг Тотошка добавил новый пост. Введите 1, чтобы посмотреть')
        view_totshka=int(input())
        mat_comment='Привет'
        mat_1_comment='Пока'
        if self.kom_mas in mat_comment or self.kom_mas in mat_1_comment:
            print('Твой друг тотошка не культурно выражается, поставь ему за это дизлайк')
            print('Для этого введите 1')
            diz_for_Totoshka=int(input())
            print('Вы поставили дизлайк Тотошке')
        if view_totshka==1:
            print(self.kom_mas, 'Время', datetime.now())
            sleep(1)
            print(self.nikname, 'Если хотите можете поставить лайк, введите 1 для того, чтобы поставить лайк')
            add_like=int(input())
            if add_like==1:
                print('Вы поставили', add_like, 'лайк на сообщение пользователя Тотошка')
                sleep(1)
            else:
                print('Листаем ленту дальше')
                sleep(1)
        else:
            print('Листаем ленту дальше')
    def Add_comment_for_Totoshka(self):
        print(self.nikname, 'Если хотите можете добавить комментарий на пост пользователя Тотошка, для этого введите 1')
        com_numbers_Totoshka=int(input())
        sleep(1)
        if com_numbers_Totoshka==1:
            print(self.nikname, 'Напишите комментарий ниже')
            com_Totshka=input()
            sleep(1)
            print('Вы добавили комментарий:', com_Totshka, 'на пост пользователя Тотошка', 'Время', datetime.now())
        else:
            print('Листаем ленту дальше')

f=Post('Denis', 1, 1, 1, 'Привет мир')
f.User_like()
f.Add_comment_for_Totoshka()