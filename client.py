import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('127.0.0.1', 10000)
#print(f"connecting to {server_address} port {server_address}")
#print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    # Send data
    message = 'PEMROGRAMAN JARINGAN TEKNIK INFORMATIKA'
    print(f"sending {message}")
    #print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message.encode())
    # Look for the respon)se
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(64)
        amount_received += len(data)
        print(f"{data}")
finally:
    print(f"closing")
    sock.close()