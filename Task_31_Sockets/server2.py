import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55555))
sock.listen(1)
conn, addres = sock.accept()
text_from_clients = conn.recv(1024).decode()
result = len(text_from_clients.split())
result_message = "Сообщение в текстовом файле - " + text_from_clients + "Количество слов в тексте - " + str(result)
conn.send(result_message.encode())