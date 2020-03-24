import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('127.0.0.1', 8889)
print(f"connecting to {server_address}")
sock.connect(server_address)

try:
    param = "list"
    param = param.encode()
    sock.send(param)
    data_file = sock.recv(2048)
    print(data_file.decode())

finally:
    print("closing list client")
    sock.close()