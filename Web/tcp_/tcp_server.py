import socket

server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
address = ("", 8000)
server_socket.bind(address)

# 可建立连接总数
server_socket.listen(128)

#返回值 socket, 元组
client_socket, client_address = server_socket.accept()
# print(client_address)
print('%s: %s connected'%client_address)

# read data
recv_data = client_socket.recv(1024)

print('received data:' + recv_data.decode('utf-8'))

client_socket.send('thanks!'.encode('utf-8'))

client_socket.close()
server_socket.close()
