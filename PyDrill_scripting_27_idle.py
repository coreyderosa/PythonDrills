##Corey DeRosa
##
##Python Course- Item 60 of 64
##
##Daily File Transfer scripting project- Python 2.7- IDLE

import shutil
import os
import glob
import time
import datetime

#moves text files from source folder to destination folder.  Uses 2 arguments within function srcDir and destDir
def copyFilesA(srcDir, destDir):
    #destDir = "C:/Users/Gowenburnett/Desktop/Folder B"
    #srcDir = "C:/Users/Gowenburnett/Desktop/Folder A/*.txt"
    for files in glob.glob(r"srcDir"):
        print files
        shutil.move(files, destDir)

#a duplicate of copyFilesA (without arguments) but moves files back into original source folder 
def copyFilesB():
    destDir = "D:\Documents\Folder A"
    for files in glob.glob(r"C:/Users/Gowenburnett/Desktop/Folder A/*.txt"): #the r in glob.glob is to escape
        print files
        shutil.move(files, destDir)

#prints the unix time a file was modified
def fileInfo():
    info = os.stat('C:/Users/Gowenburnett/Desktop/Folder A/random1.txt')
    print info
    print info.st_mtime

#makes a list of files in a folder
def makeList():
    fileList =[]
    fileDir = 'C:/Users/Gowenburnett/Desktop/Folder A/'
    for files in os.listdir(fileDir):
        print files
        fileInfo = os.stat(os.path.join(fileDir, files)) #joins the file and the directory into one string
        fileList.append([files, time.ctime(fileInfo.st_mtime)]) #creates a list of the file and directory path
    #return fileList
        for files in fileList:
            print fileInfo.st_mtime, files
        #if fileInfo.st_mtime <=

#will print the converted unix time file was modified into hours and minutes
def findTime(unixTime):
    print datetime.fromtimestamp(unixTime).strftime('%H:%M')

#attempting to get the current time and the time random1.txt was modified.
#attempting to get these times in the same format.  unix or clock format or whatever as long as they're the same
def random1():
    random1info = os.stat('C:/Users/Gowenburnett/Desktop/Folder A/random1.txt') #gets random1.txt file info
    random1time = random1info.st_mtime #gets the time random1.txt was modified
    d = time.localtime() #shows local time broken up into year, month, day, hour, etc.
    
    #print datetime.datetime.fromtimestamp(random1time).strftime("%H:%M") #convert the time random1.txt to hour:minute
    print d.tm_hour #shows local time hour
##    if random1info.st_mtime < datetime.now:
##        print true
##    else:
##        print false

#copyFilesA()
#copyFilesB()
#fileInfo()
makeList()
#random1()
