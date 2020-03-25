# Tugas 4

## Cara Kerja

Setelah menjalankan file_server.py, jalankan client yang diinginkan.

### Download Client
Agar dapat mendownload file, masukkan nama file yang diinginkan. Kemudian program akan mengirimkan parameter dengan format
```
download [spasi] nama_file
```
ke file_server. File server kemudian akan mengirimkan filenya dan kemudian diterima oleh client. Respon yang diterima dapat dilihat pada gambar dibawah.

![Download Client](screenshots/download.PNG?raw=true)

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
Agar dapat mengupload file, masukkan nama file yang ingin di upload. Kemudian program akan mengirimkan parameter dengan format
```
upload [spasi] nama_file [spasi] isi_file
```
ke file_server. File server kemudian akan menerima data yang telah dikirim oleh client dan menyimpannya. Respon yang diterima dapat dilihat pada gambar dibawah.

![Upload Client](screenshots/upload.PNG?raw=true)
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
Untuk melihat file apa saja yang terdapat di dalam folder 'folder', jalankan client_list.py. Program akan mengirimkan parameter dengan format
```
list
```
ke file_server. File server kemudian akan mengirimkan data berupa JSON ke client. Respon dari client list adalah seperti gambar dibawah

![Upload Client](screenshots/list.PNG?raw=true)
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
