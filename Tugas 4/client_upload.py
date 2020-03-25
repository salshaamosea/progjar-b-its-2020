import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('127.0.0.1', 8889)
print(f"connecting to {server_address}")
sock.connect(server_address)

file_name = input("Masukkan nama file yang ingin di upload: ")

try:
    temp = open(file_name, "rb")
    isi_file = temp.read(2048)
    isi_file = isi_file.decode()

    param = "upload " + file_name + " " + isi_file
    param = param.encode()
    sock.send(param)

finally:
    print("success uploading file")
    print("closing upload client")
    sock.close()
