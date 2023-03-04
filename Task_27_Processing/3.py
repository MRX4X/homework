from multiprocessing import Process, Pipe
import time

def currency(conn, n):
    conn.send(n)
    conn.close()

if __name__ == '__main__':
    parent_conf, child_conf=Pipe()
    p1=Process(target=currency, args=(child_conf, 75))
    time.sleep(1)
    p1.start()
    print(parent_conf.recv())
