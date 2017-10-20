import socket

server_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

server_addr = ('archlinux', 8080)
server_sock.bind(server_addr)

while True:
    receive_data, client_addr = server_sock.recvfrom(1024)
    msg = receive_data.decode('utf-8')
    print(client_addr, ": ", msg)
    if msg == 'quit':
        server_sock.close()
        break
print('exit')
