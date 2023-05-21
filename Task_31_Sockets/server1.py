import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55555))
sock.listen(1)
print('The server is on, you can start chatting')
conn, addres = sock.accept()
print('connected', addres)
while True:
    data = conn.recv(1024).decode()
    print(data)
    if data=='пока':
        break
    message=input(" -> ")
    conn.send(message.encode())
    if message=='пока':
        break
conn.close()
