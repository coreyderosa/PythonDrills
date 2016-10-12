##Corey DeRosa
##
##Python Course- Item 59 of 64
##
##File Mover- Python 2.7- IDLE

import shutil
import os

import shutil
import os

def moveFiles():
    file1 = "C:\\Users\\Gowenburnett\\Desktop\\Folder A\\random1.txt"
    file2 = "C:\\Users\\Gowenburnett\\Desktop\\Folder A\\random2.txt"
    file3 = "C:\\Users\\Gowenburnett\\Desktop\\Folder A\\random3.txt"
    file4 = "C:\\Users\\Gowenburnett\\Desktop\\Folder A\\random4.txt"
    dst = "C:\\Users\\Gowenburnett\\Desktop\\Folder B"
    shutil.move(file1,dst)
    shutil.move(file2,dst)
    shutil.move(file3,dst)
    shutil.move(file4,dst)
    print os.path.realpath(file1)
    print os.path.realpath(file2)
    print os.path.realpath(file3)
    print os.path.realpath(file4)

moveFiles()


