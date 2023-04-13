from threading import Thread
import socket
import psycopg2

conn_bd_user = psycopg2.connect(dbname='user_for_chat', user='denis', password='7278', host='localhost')
cur = conn_bd_user.cursor()


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
            conn.send('Введите логин и пароль для регистрации'.encode())
            conn.send('Введите логин'.encode())
            user_mas=[]
            login_user= conn.recv(1024).decode()
            user_mas.append(login_user)
            conn.send('Введите пароль'.encode())
            pass_user = conn.recv(1024).decode()
            user_mas.append(pass_user)
            print(user_mas)
            insert_query = """ INSERT INTO user_for_chat (login_user, pass_user)
                                          VALUES (%s, %s)"""
            item_tuple = (user_mas[0], user_mas[1])
            cur.execute(insert_query, item_tuple)
            conn_bd_user.commit()
            print("1 элемент (строка) успешно добавлен")
            cur.execute("SELECT login_user, pass_user from user_for_chat where login_user = %s", [login_user])
            purchase_user = cur.fetchone()
            conn_bd_user.commit()

            if user_mas[0]==purchase_user[0] and user_mas[1]==purchase_user[1]:
                conn.send('Вы успешно зарегистрировались, подключение осуществленно'.encode())
                break
            else:
                conn.send('Логин должен быть уникальным, регистрация не возможна, перезагрузите клиент'.encode())

        if message_user=='2':
            conn.send('Введите логин и пароль для регистрации'.encode())
            conn.send('Введите логин'.encode())
            user_mas = []
            login_user = conn.recv(1024).decode()
            user_mas.append(login_user)
            conn.send('Введите пароль'.encode())
            pass_user = conn.recv(1024).decode()
            user_mas.append(pass_user)
            print(user_mas)
            cur.execute("SELECT login_user, pass_user from user_for_chat where login_user = %s", [login_user])
            purchase_user = cur.fetchone()
            conn_bd_user.commit()
            if user_mas[0]==purchase_user[0] and user_mas[1]==purchase_user[1]:
                conn.send('Логин и пароль введен верно, подключение осуществленно'.encode())
                break
            else:
                conn.send('Вы не правильно ввели логин или пароль, перезагрузите клиент'.encode())


while True:
    conn, addr = sock.accept()
    print(f'Подключился:{addr}')
    clients.add(conn)
    autorisation(conn)
    print('После регистрации, перед созданием потока с сообщениями, в котором функция отправки сообщений клиентам')
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
