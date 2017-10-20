import socket
from threading import Thread


# 处理客户端的请求并执行事情
def handle_client(client_sock, client_addr):
    while True:
        recv_data = client_sock.recv(1024)
        if len(recv_data) > 0:
            print('recv[%s]:%s' % (str(client_addr), recv_data.decode()))
        else:
            print('[%s]客户端已经关闭' % str(client_addr))
            break

    client_sock.close()


def main():

    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    address = ('', 8000)
    server_sock.bind(address)
    server_sock.listen(128)

    while True:
        print('-----主线程，，等待新客户端的到来------')
        client_sock, client_addr = server_sock.accept()

        print('-----主线程，，接下来创建一个新的线程负责数据处理[%s]-----' % str(client_addr))
        thread = Thread(target=handle_client, args=(client_sock, client_addr))
        thread.start()

        # 因为线程中共享这个套接字，如果关闭了会导致这个套接字不可用，
        # 但是此时在线程中这个套接字可能还在收数据，因此不能关闭
        # client_sock.close()

    server_sock.close()

if __name__ == '__main__':
    main()
