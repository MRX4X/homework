from threading import Thread
import socket
import psycopg2

conn = psycopg2.connect(dbname='user_for_chat', user='denis', password='7278', host='localhost')
cursor = conn.cursor()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # создаем сокет для сервера
sock.bind(('localhost', 55000))
sock.listen(10)


clients = set() #Множество сокетов для подключения
def connection(soc_cl):
    while True:
        print('Начало соединения, функция connection')
        massage = soc_cl.recv(1024)
        global clients
        print('Перед циклом функция connection')
        for i in clients:
            i.send(massage)
            print('Отправка после каждого сообщения')

def autorisation(conn):
    while True:
        conn.send('Выберите, хотите вы зарегистрироваться - 1 или войти - 2'.encode())
        message_user=conn.recv(1024).decode()
        print('Начало регистрации, перед выбором регистрации или входа')
        if message_user=='1':
            conn.send('Введите логин и пароль для регистрации в строчку через запятую'.encode())
            message_mas=conn.recv(1024).decode().split(',')
            if message_mas[0]=='denis' and message_mas[1]== '123':
                conn.send('Логин и пароль введен верно, подключение осуществленно'.encode())
                break
            else:
                conn.send('Вы не правильно ввели пароль, перезагрузите клиент'.encode())

        if message_user=='2':
            conn.send('Введите логин и пароль для того, чтобы зайти'.encode())
            message_mas=conn.recv(1024).decode().split(',')
            if message_mas[0]=='denis' and message_mas[1]== '123':
                conn.send('Логин и пароль введен верно, подключение осуществленно'.encode())
                break
            else:
                conn.send('Вы не правильно ввели пароль, повторите попытку еще раз'.encode())

while True:
    conn, addr = sock.accept()
    print(f'Подключился:{addr}')
    clients.add(conn)
    autorisation(conn)
    print('После регистрации, перед созданием потока с сообщениями, в котором функция отправки сообщщений клиентам')
    if conn:
        th1 = Thread(target=connection, args=(conn,), daemon=True)
        th1.start()







# СЕРВЕР БЕЗ РЕГИСТРАЦИИ, ТОЛЬКО ПРИНИМАЕТ И ОТПРАВЛЯЕТ СООБЩЕНИЯ.
# from threading import Thread
# import socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # создаем сокет для сервера
# sock.bind(('localhost', 55000))
# sock.listen(10)
#
# clients = set() #Множество сокетов для подключения
# def connection(soc_cl):
#     while True:
#         massage = soc_cl.recv(1024)
#         global clients
#         for i in clients:
#             i.send(massage)
#
#
# while True:
#     conn, addr = sock.accept()
#     print(f'Подключился:{addr}')
#     clients.add(conn)
#     if conn:
#         th = Thread(target=connection, args=(conn,), daemon=True)
#         th.start()