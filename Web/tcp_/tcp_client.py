import socket

client_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
server_address = ('archlinux', 8000)

client_sock.connect(server_address)
msg = input('input your message:')

client_sock.send(msg.encode('utf-8'))

recv_data = client_sock.recv(1024)
print('get data: %s'%recv_data.decode())

client_sock.close()
