from queue import Queue
from threading import Thread

def read_names(my_que):
    with open('names.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            my_que.put('/Users/denis/homework/Task_26_ThreadPool/'+line.strip())
        my_que.put('off')
my_que = Queue()
def makedir(my_que):
    while True:
        a=my_que.get()
        if a=='off':
            break
        open(f'{a}.txt', 'w')

threads_1 = Thread(target=read_names, args=(my_que, ))
threads_1.start()
threads_2 = Thread(target=makedir, args=(my_que,))
threads_2.start()