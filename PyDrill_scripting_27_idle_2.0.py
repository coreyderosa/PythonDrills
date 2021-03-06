##Corey DeRosa- Python Course Item 60
##
##PyDrill_scripting27_idle
##
##Daily File Transfer scripting project- Python 2.7- IDLE

from datetime import datetime, timedelta
import os
import time
import shutil
from glob import glob

#copys file if modified time is larger than 24 hours ago
def timeCompare(fileSrc, fileDest):
    currentTime = datetime.now() #gives us the current time
    time24hoursAgo = currentTime - timedelta(hours = 24) #finds the time 24 hours from current time
    for f in os.listdir(fileSrc): #glob shows the entire file path
        files = os.path.realpath(os.path.join(fileSrc,f)) #shows the file's path then joins the file's path and the directory's paths.  This provides the datetime with the entire file's path
        if files.endswith('.txt'):
            fileSrcModifiedTime = datetime.fromtimestamp(os.path.getmtime(files)) #gives us each file's modified time
            if fileSrcModifiedTime > time24hoursAgo: #if file's modified time is greater than 24 hours old copy file to destination folder
                print files, "copied to: ", fileDest
                shutil.copy(files,fileDest) #copys file to destination
            else:
                print files, "not copied"

fileSrc = 'D:\Documents\Folder A\*.txt'
#fileSrc = 'D:\Documents\Folder A'            
fileDest = 'D:\Documents\Folder B'
timeCompare(fileSrc, fileDest) #2 arguments required (Source folder with \*.txt, Destination folder)
