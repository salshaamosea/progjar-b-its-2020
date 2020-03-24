from handler import Handler
import json
import logging

'''
PROTOCOL FORMAT

string terbagi menjadi 2 bagian, dipisahkan oleh spasi
COMMAND spasi PARAMETER spasi PARAMETER ...

FITUR

- create : untuk membuat record
  request : create
  parameter : nama spasi notelpon
  response : berhasil -> ok
             gagal -> error

- delete : untuk menghapus record
  request: delete
  parameter : id
  response: berhasil -> OK
            gagal -> ERROR

- list : untuk melihat daftar record
  request: list
  parameter: tidak ada
  response: daftar record person yang ada

- get : untuk mencari record berdasar nama
  request: get 
  parameter: nama yang dicari
  response: record yang dicari dalam bentuk json format

- jika command tidak dikenali akan merespon dengan ERRCMD

'''
p = Handler()

class FileMachine:
    def proses(self,string_to_process):
        s = string_to_process
        cstring = s.split(" ", 2)
        try:
            command = cstring[0].strip()
            if (command=='upload'):
                logging.warning("upload")
                file_name = cstring[1].strip()
                isi_file = cstring[2].strip()
                p.upload_data(file_name, isi_file)
                return "OK"
            elif (command=='list'):
                logging.warning("list")
                ls = {}
                ls['File List'] = []
                list_file = p.list_data()
                no_file = 0
                for file_name in list_file:
                    no_file += 1
                    ls['File List'].append({no_file:file_name})
                return json.dumps(ls, indent=2)
            elif (command=='download'):
                logging.warning("download")
                file_name = cstring[1].strip()
                isi_file = p.get_data(file_name)
                # return json.dumps(isi_file)
                return isi_file
            else:
                return "ERRCMD"
        except:
            return "ERROR"


if __name__=='__main__':
    pm = FileMachine()