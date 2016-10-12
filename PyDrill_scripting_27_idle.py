##Corey DeRosa
##
##Python Course- Item 60 of 64
##
##Daily File Transfer scripting project- Python 2.7- IDLE

import shutil
import os
import glob
import time

##def copyFilesA():
##    destDir = "C:/Users/Gowenburnett/Desktop/Folder B"
##    for file in glob.glob(r"C:/Users/Gowenburnett/Desktop/Folder A/*.txt"):
##        print file
##        shutil.move(file, destDir)
##
##def copyFilesB():
##    destDir = "C:/Users/Gowenburnett/Desktop/Folder A"
##    for file in glob.glob(r"C:/Users/Gowenburnett/Desktop/Folder B/*.txt"):
##        print file
##        shutil.move(file, destDir)
##
##copyFilesA()
###copyFilesB()

def fileInfo():
    info = os.stat('C:/Users/Gowenburnett/Desktop/Folder A/random1.txt')
    print info
    print info.st_mtime

fileInfo()
