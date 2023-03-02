from queue import Queue
from threading import Thread
def familia(que):
    while True:
        familia=input()

        if familia=='off':
            break

        que.put(familia)


def kik(que):
    print(que.qsize())
    while True:
        try:
            name=que.get()
        except que.Empty:
            continue
        else:
            print(name, 'отчислен')
        que.task_done()


queue = Queue()
queue.put("ivanov")
t1=Thread(target=familia, args=(queue, ))
t1.start()
t2=Thread(target=kik, args=(queue, ), daemon=True)
t2.start()

