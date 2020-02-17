import sys
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 31000)
print(f"starting up on {server_address}")
sock.bind(server_address)

#listen for incoming connection
sock.listen(1)

while True:
    #wait for connection
    print(f"waiting for connection")
    connection, client_address = sock.accept()
    print(f"connection from {client_address}")
    while True:
        data = connection.recv(128)
        print(f"received {data.decode()}")
        if data:
            print(f"sending data back")
            connection.sendall(data)
        else:
            # print(f"no more data from {client_address}")
            break
    #clean up connection
    connection.close()
