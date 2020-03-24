import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('127.0.0.1', 8889)
print(f"connecting to {server_address}")
sock.connect(server_address)

file_name = input("Masukkan nama file yang ingin di download: ")

try:
    param = "download " + file_name
    param = param.encode()
    sock.send(param)

    data_file = sock.recv(2048)
    isi_file = open(file_name, 'wb')
    isi_file.write(data_file)
    isi_file.close()

finally:
    print("closing download client")
    sock.close()
