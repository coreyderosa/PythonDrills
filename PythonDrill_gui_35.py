##Corey DeRosa- Python Course Item 60
##
##PyDrill_gui_34_idle
##
##UI for File Transfer project- Python 3.5.2- IDLE

from tkinter import *
from tkinter import ttk as ttk, messagebox, filedialog
from datetime import datetime, timedelta
import os
import time
import shutil
from glob import glob
##from tkinter import ttk
##from tkinter import messagebox

root =Tk()

style  = ttk.Style()

style.theme_use('classic')

#Daily folder Browse Window
def selectDailyFolder(root):
    root.dailyFolder = filedialog.askdirectory(initialdir = "D:\Documents", title = "Select your Daily Folder") #opens dialog box in Documents folder
    dailyFolder = root.dailyFolder
    #print(root.dailyFolder)
    dailyLabel = ttk.Label(root, text = dailyFolder ) #prints selected folder path on label
    dailyLabel.grid(row = 5, column = 1)
    dailyLabel.config(foreground = "blue")


#Destination folder Browse Window
def selectDestFolder(root):
    root.destFolder = filedialog.askdirectory(initialdir = "D:\Documents", title = "Select your Destination Folder") #opens dialog box in Documents folder
    destFolder = root.destFolder
    #print(root.destFolder)
    destLabel = ttk.Label(root, text = destFolder) #prints selected folder path on label
    destLabel.grid(row = 5, column = 2, rowspan = 2)
    destLabel.config(foreground = "blue")


#Gets the file's modified time then time 24 hours ago
#Finds each file's path
#And if the file's extension = .txt and modified time is larger than 24 hours ago
#It copies the file to destination folder
def timeCompare(fileSrc, fileDest):
    currentTime = datetime.now() #gives us the current time
    time24hoursAgo = currentTime - timedelta(hours = 24) #finds the time 24 hours from current time
    for f in os.listdir(fileSrc): #glob shows the entire file path
        files = os.path.realpath(os.path.join(fileSrc,f)) #shows the file's path then joins the file's path and the directory's paths.  This provides the datetime with the entire file's path
        if files.endswith('.txt'):
            fileSrcModifiedTime = datetime.fromtimestamp(os.path.getmtime(files)) #gives us each file's modified time
            if fileSrcModifiedTime > time24hoursAgo: #if file's modified time is greater than 24 hours old copy file to destination folder
                print (files, "copied to: ", fileDest)
                shutil.copy(files,fileDest) #copys file to destination
            else:
                print (files, "not copied")


#Buttons
dailyButton = ttk.Button(root, text = "Choose the 'Checked Daily' folder...", command = lambda: selectDailyFolder(root))
dailyButton.grid(row = 3, column = 1, rowspan = 2)

destButton = ttk.Button(root, text = "Choose the 'Destination' folder...", command = lambda: selectDestFolder(root))
destButton.grid(row = 3, column = 2, rowspan = 2)

initiateButton = ttk.Button(root, text = "'File Check'" , command = lambda: timeCompare(dailyFolder, destFolder))
initiateButton.grid(row = 3, column = 3, rowspan = 2)

#Labels
dailyFolder = filedialog.askdirectory(initialdir = "D:\Documents", title = "Select your Daily Folder") #opens dialog box in Documents folder
dailyLabel = ttk.Label(root, text = dailyFolder ) #prints selected folder path on label
dailyLabel.grid(row = 5, column = 1)
dailyLabel.config(foreground = "blue")

destFolder = filedialog.askdirectory(initialdir = "D:\Documents", title = "Select your Destination Folder") #opens dialog box in Documents folder
destLabel = ttk.Label(root, text = destFolder) #prints selected folder path on label
destLabel.grid(row = 5, column = 2, rowspan = 2)
destLabel.config(foreground = "blue")


#fileSrc = r'D:\Documents\Folder A\*txt'
#fileDest = r'D:\Documents\Folder B'
##timeCompare(fileSrc, fileDest) #2 arguments required (Source folder with \*.txt, Destination folder)

root.mainloop()

