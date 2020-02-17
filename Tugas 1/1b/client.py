import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('127.0.0.1', 30001)
#print(f"connecting to {server_address} port {server_address}")
#print >>sys.stderr, 'connecting to %s port %s' % server_address
nama_file = input("Nama file yang diinginkan : ")
print(f"connecting to {server_address}")
sock.connect(server_address)

try:
    # Send data
    print(f"sending {nama_file}")
    sock.sendall(nama_file.encode())
    while True:
        data = sock.recv(1024)
        file = open("NEW_" + nama_file, 'a+b')
        if not data:
            file.close()
            break
        file.write(data)

finally:
    print(f"closing")
    sock.close()
