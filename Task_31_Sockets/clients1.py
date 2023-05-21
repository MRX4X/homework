import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((socket.gethostname(), 55555))
print('The connection is established, you can start chatting')
# message = input(" -> ")
while True:
    message = input(" -> ")
    sock.send(message.encode())
    if message=='пока':
        break
    data = sock.recv(1024).decode()
    if data=='пока':
        break
    print(data)
sock.close()