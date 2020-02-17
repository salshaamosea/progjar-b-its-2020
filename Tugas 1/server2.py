import sys
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 30002)
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

# import sys
# import socket
# # Create a TCP/IP socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # Bind the socket to the port
# server_address = ('localhost', 10000)
# print >>sys.stderr, 'starting up on %s port %s' % server_address
# sock.bind(server_address)
# # Listen for incoming connections
# sock.listen(1)
# while True:
#     	# Wait for a connection
#     	print(sys.stderr, 'waiting for a connection')
#     	connection, client_address = sock.accept()
#     	print >>sys.stderr, 'connection from', client_address
#     	# Receive the data in small chunks and retransmit it
#     	while True:
#         	data = connection.recv(32)
#         	print >>sys.stderr, 'received "%s"' % data
#             	if data:
#                 	print >>sys.stderr, 'sending data back to the client'
#                 	connection.sendall('-->'+data)
#             	else:
#                 	print >>sys.stderr, 'no more data from', client_address
#                 	break
#         # Clean up the connection
# 	connection.close()