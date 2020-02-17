import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('127.0.0.1', 30001)
#print(f"connecting to {server_address} port {server_address}")
#print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    # baca file
    f_name = "test.txt"
    temp = open(f_name, "rb")
    # data->server
    file = temp.read()
    print('Sending data to Server')
    sock.send(file)

finally:
    print(f"closing")
    sock.close()
