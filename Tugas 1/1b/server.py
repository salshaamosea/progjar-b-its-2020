import sys
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 30001)
print(f"starting up on {server_address}")
sock.bind(server_address)

#listen for incoming connection
sock.listen(1)

while True:
    # Wait for a connection
    print("waiting for a connection")
    connection, client_address = sock.accept()
    print(f"connection from {client_address}")
    # Receive the data in small chunks and retransmit it
    data = connection.recv(1024)
    file = open(data.decode(), "rb")
    read = file.read()
    connection.sendall(read)
    file.close()
    print("sent")
    #clean up connection
    connection.close()
