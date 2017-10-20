import socket

server_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
server_addr = ('', 8053)
server_sock.bind(server_addr)

domain_ip = {
    "www.itcast.cn": "192.168.1.2",
    "www.itheima.com": "192.168.1.3",
    "www.google.com": "192.168.1.4",
}

while True:
    receive_data, client_addr = server_sock.recvfrom(1024)
    domain = receive_data.decode('utf-8')
    print(client_addr, ':', domain)
    ip = domain_ip.get(domain, "I don't know.")
    server_sock.sendto(ip.encode('utf-8'), client_addr)
