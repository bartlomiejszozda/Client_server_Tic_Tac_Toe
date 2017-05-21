import socket
import sys
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address=('localhost',10000)
sys.stderr.write('connecting to port {}' .format(server_address))
sock.connect(server_address)


try:
    while True:
        data=sock.recv(512)
        print(data.decode())
        if "dzieki za gre" in data.decode():
            break
        message=input()
        sock.send(str.encode(message))

finally:
    sys.stderr.write('closing socket')
    sock.close()
