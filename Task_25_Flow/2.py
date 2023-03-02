import time
from threading import Thread

def Demon():
    while True:
        time.sleep(3)
        print('вводите быстрее')

dem=Thread(target=Demon, daemon=True)
dem.start()


cod=777
cod_bomb=int(input('Введите код'))
if cod_bomb==cod:
    print('Бомба разминированна')
elif cod_bomb!=cod:
    print('Вы взорвались')
