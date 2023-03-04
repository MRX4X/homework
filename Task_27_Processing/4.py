import random
import sys
import time
import multiprocessing

def guess_the_number():
    print('Приветствуем тебя в игре "Угадай число". Тебе нужно вводить числа от нуля до ста, пока не угаадешь')
    random_number=random.randint(0, 100)
    while True:
        number_user = int(input('Вводи число - '))
        if number_user!=random_number:
            print('Мы загадали другое число, вводи заново')
        else:
            print('Ты угадал')
            sys.exit('Игра завершена')

def subscription():
    sec = 0
    if sec==5:
        print('Подписка кончилась, оплати занова, чтобы играть')
        sys.exit()
    while True:
        time.sleep(1)
        sec += 1


if __name__ == '__main__':
    p1=multiprocessing.Process(target=guess_the_number())
    p2=multiprocessing.Process(target=subscription())
    p1.start()
    p2.start()