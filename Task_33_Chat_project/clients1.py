import socket
from threading import Thread
from datetime import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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



#Добавление базы данных в программный код
# import psycopg2
#
# conn = psycopg2.connect(dbname='postgres', user='denis', password='7278', host='localhost')
# cursor = conn.cursor()
