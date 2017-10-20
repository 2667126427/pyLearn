import socket

client_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

server_addr = ('archlinux', 8053)
domain = input('enter the domain to query:')

while domain and domain != 'quit':
    client_sock.sendto(domain.encode('utf-8'), server_addr)
    ip = client_sock.recv(1024)
    print('ip:' + ip.decode('utf-8'))
    domain = input('enter the domain to query:')
