import time
from threading import Thread


def napominalka():
    message=input()
    sec=int(input())
    time.sleep(sec)
    print(message)

t1=Thread(target=napominalka)
t1.start()
time.sleep(10)
print('Программа завершается')
