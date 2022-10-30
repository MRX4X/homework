from time import *
start=time()
while True:
    a=int(input())
    b=30
    end=time()
    total=end-start
    c=b-total
    print('Осталось минут', c)
    if total==30 or a==0:
        print('игра окочена')
        break