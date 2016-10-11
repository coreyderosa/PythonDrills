##Corey DeRosa
##
##Python Course- Item 59 of 64
##
##File Mover- Python 2.7- IDLE

import shutil
def moveFiles():
	src = "C:\\Users\Gowenburnett\\Desktop\\Folder A\\random1.txt"
	dst = "C:\Users\\Gowenburnett\\Desktop\\Folder B\\random1.txt"
	shutil.move(src,dst)
	print 'This is the original file path: ', src
	print 'This is the new file path: ',dst

moveFiles()
