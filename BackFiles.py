import shutil
import os

source = input("Enter Source folder name: ")
destination = input("Enter Destination folder name: ")

source = source + '/'
destination = destination + '/'

list_of_files=os.listdir(source)

for file in list_of_files:
    shutil.copy((source + file),destination)