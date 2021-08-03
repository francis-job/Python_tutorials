import socket

def connect(hostname, port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = sock.connect_ex((hostname, port))
    print("my ip is: ",sock.getsockname()[0])
    sock.close()
    return result == 0

for i in range(0,255):
    res = connect("192.168.5."+str(i), 80)
    if res:
        print("Device found at: 192.168.5."+str(i) + ":"+str(80))
