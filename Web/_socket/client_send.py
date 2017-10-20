import socket

client_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

server_addr = ('archlinux', 8080)

data = input('please enter some word:')

while data:
    client_sock.sendto(data.encode('utf-8'), server_addr)
    data = input('please enter some word:')

client_sock.close()
