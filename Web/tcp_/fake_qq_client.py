import socket

# 创建socket
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 链接服务器
server_addr = ('127.0.0.1', 8000)
client_sock.connect(server_addr)

while True:

    # 提示用户输入数据
    msg = input("请输入要发送的消息：")

    # 若用户输入了内容，则发送，否则退出
    if len(msg) > 0:
        client_sock.send(msg.encode())

        # 接收对方发送过来的数据，最大接收1024个字节
        recv_data = client_sock.recv(1024)
        print("收到的消息：%s" % recv_data.decode())
    else:
        break

# 关闭套接字
client_sock.close()