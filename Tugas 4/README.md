# Tugas 4

One Paragraph of project description goes here

## Cara Kerja

Setelah menjalankan file_server.py, jalankan client yang diinginkan.

### Download Client
Agar dapat mendownload file, masukkan nama file yang diinginkan.

```
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

```

### Upload Client
```
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
    print("closing")
    sock.close()
```

### List Client
```
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
```
