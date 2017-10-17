#!/usr/bin/python3
import socket
# import sys

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
host = socket.gethostname()
port = 9999

server_socket.bind((host, port))
server_socket.listen(5)

while True:
    client_socket, addr = server_socket.accept()
    print("Addr: {0}:{1}".format(client_socket, addr))
    msg = "Welcome to my website!"
    client_socket.send(msg.encode('utf-8'))
    client_socket.close()

