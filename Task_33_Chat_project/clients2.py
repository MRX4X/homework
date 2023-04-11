# import socket
# from threading import Thread
# from datetime import datetime
#
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# name = input('Введите имя: ')
# sock.connect(('localhost', 55000))
#
# def accept():
#     while True:
#         data = sock.recv(1024)
#         print(data.decode())
#
# th = Thread(target=accept)
# th.start()
#
# while True:
#     text = input()
#     dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     sock.send(bytes(dt + ' ' + name + ':' + text, encoding='UTF-8'))










import socket
from threading import Thread
from datetime import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# name = input('Введите имя: ')
sock.connect(('localhost', 55000))

def accept():
    while True:
        data = sock.recv(1024)
        print(data.decode())

th = Thread(target=accept)
th.start()

while True:
    text = input()
    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sock.send(bytes(text, encoding='UTF-8'))