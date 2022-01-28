import shutil
import os

path = input("Enter the name of the directory to be sorted: ")
list_of_files = os.listdir(path)
for file in list_of_files:
    name,ext = os.path.splitext(file)
    ext = ext[1:]
    #this force the next iteration if it is the directory  
    if(ext==''):
        continue
    
    if(os.path.exists(path + '/' + ext)):
        shutil.move(path + '/' + file , path + '/' + ext + '/' + file)

    else:
        os.mkdir(path + '/' + ext)
        shutil.move(path + '/' + file , path + '/' + ext + '/' + file)