import socket, traceback, time, struct

host = ''
port = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))

while True:
    try:
        message, address = s.recvfrom(8192)
        secs = int(time.time()) # seconds since 1/1/1970
        secs -= 60 * 60 * 24    # make it yesterday
        secs += 2208988800  # convert to seconds since 1/1/1900
        reply = struct.pack("!I", secs)
        s.sendto(reply, address)
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()
