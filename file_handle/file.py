

import os

class FileManger():

    def create_dir(self, name, address):
        path = address
        if path[-1] != '/':
            path +='/'
        try:  
            os.mkdir(path + name)
        except OSError:  
            print("Creation of the directory {} failed".format(path))
        else:  
            print("Successfully created the directory {} ".format(path))

    def create_file(self, name, address):
        path = address
        if path[-1] != '/':
            path +='/'
        try:
            fh = open(path + name, 'r')
        except:
            fh = open(path + name, 'w+')
            print("Successfully created the file {} ".format(path + name))
        else:
            print("Creation of the file {} failed".format(path + name))

    def delete_file(self, name, address):
        path = address
        if path[-1] != '/':
            path +='/'
        try:
            os.remove(path + name)
        except:
            print("Deletion of the file {} failed".format(path + name))
        else:
            print("Successfully deleted the file {} ".format(path + name))

    def find(self, name, address):
        address_list = []
        for dirpath, dirnames, filenames in os.walk(address):
            for filename in [f for f in filenames if f==name]:
                address_list.append(os.path.join(dirpath, filename))
        return address_list

f = FileManger()

f.create_dir('new_mostafa','/home/ariana/Desktop/mostafa2')
f.create_file('myfile2','/home/ariana/Desktop/mostafa2/new_mostafa')
print(f.find('myfile2','/home/ariana/Desktop/mostafa2'))
# f.delete_file('myfile','/home/ariana/Desktop/mostafa2/new_mostafa')
