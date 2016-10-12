##Corey DeRosa
##
##Python Course- Item 59 of 64
##
##File Mover- Python 2.7- IDLE

import shutil
import glob

def moveFiles():
    destDir = "C:/Users/Gowenburnett/Desktop/Folder B"
    for file in glob.glob(r"C:/Users/Gowenburnett/Desktop/Folder A/*.txt"):
        print file
        shutil.move(file, destDir)

moveFiles()
