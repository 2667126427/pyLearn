import socket, traceback

host = ''
port = 54321

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

while True:
    try:
        client_sock, client_addr = s.accept()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue

    # process the connection
    try:
        print("Got connection from", client_sock.getpeername())
        # process the requests here
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()

    #close connection
    try:
        client_sock.close()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
