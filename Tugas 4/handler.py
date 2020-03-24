import shelve
import uuid
import os
import base64

class Handler:
    def __init__(self):
        # self.data = shelve.open('mydata.dat')
        if not os.path.exists('folder'):
            os.makedirs('folder')
    def upload_data(self, file_name = None, isi_file = None):
        temp = open('folder/' + file_name, 'w')
        temp.write(isi_file)
        return True
    def get_data(self, file_name = None):
        temp = open('folder/' + file_name, 'rb')
        isi_file = temp.read()
        temp.close()
        isi_file = isi_file.decode()
        return isi_file
    def list_data(self):
        list_file = os.listdir('folder')
        temp = []
        for file_name in list_file:
            temp.append(file_name)
        return temp

if __name__=='__main__':
    p = Handler()
