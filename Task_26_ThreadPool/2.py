from queue import Queue
from threading import Thread

def delitel(que):
    while True:
        number=que.get()
        result=[]
        for i in range(1, number + 1):
            if number % i == 0:
                result.append(i)
        que.task_done()
        a=number
        if a==228:
            break
        print(result)
        result.clear()


my_queue = Queue()
my_queue.put(10)
my_queue.put(20)
my_queue.put(18)
my_queue.put(228)
threads = Thread(target=delitel, args=(my_queue,))
threads.start()