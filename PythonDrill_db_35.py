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
import sqlite3

######################### Create Database ############################

#creates database
def firstRundb():
    db = sqlite3.connect('test.db')
    print('Opened database successfully!')
    db.execute('DROP TABLE IF EXISTS fcRuns')
    db.execute('CREATE TABLE IF NOT EXISTS fcRuns (ID INTEGER PRIMARY KEY AUTOINCREMENT, fcTime TEXT)')
    print ('Created table successfully!')
    db.commit()


class FileCheck:

    def __init__(self, master):

################################ GUI ################################
        #Frame for header
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        
        #Daily Folder
        self.dailyFolderName = StringVar()
        print (self.dailyFolderName)
        self.daily = (self.dailyFolderName.get())
        
        #Destination Folder
        self.destFolderName = StringVar()
        print (self.destFolderName)
        self.dest = (self.destFolderName.get())

        self.fcTimestamp = StringVar()
        print (self.fcTimestamp)
        self.fcT = (self.fcTimestamp.get())
        
        #logo and header
        self.logo = PhotoImage(file = "D:\Documents\School\Tech Academy\Portfolio\coco logo.png")
        headerLabel = ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, columnspan = 2, pady = 5, sticky = 'w')
        titleLabel = ttk.Label(self.frame_header, text = 'Welcome to File Check.  File transfer made easy! ', font = 'bold')
        titleLabel.grid(row = 0, column = 0, columnspan = 2, pady = 5, sticky = 'w')

        #Frame for labels and buttons
        self.frame_steps = ttk.Frame(master)
        self.frame_steps.pack()

        #step labels
        dailyStepLabel = ttk.Label(self.frame_steps, text = 'Step 1- Choose Daily Folder')
        dailyStepLabel.grid(row = 0, column = 0, columnspan = 2, pady = 5, sticky = 'w')
        destStepLabel = ttk.Label(self.frame_steps, text = 'Step 2- Choose Destination Folder')
        destStepLabel.grid(row = 3, column = 0, columnspan = 2, pady = 5, sticky = 'w')
        initiateStepLabel = ttk.Label(self.frame_steps, text = 'Step 3- Initiate File Check')
        initiateStepLabel.grid(row = 7, column = 0, columnspan = 2, pady = 5, sticky = 'w')
        
        #buttons   
        dailyButton = ttk.Button(self.frame_steps, text = 'Daily Folder', command = self.selectDailyFolder)
        dailyButton.grid(row = 1, column = 0, sticky = 'w')
        destButton = ttk.Button(self.frame_steps, text = 'Destination Folder', command = self.selectDestFolder)
        destButton.grid(row = 4, column = 0, sticky = 'w')
        initiateButton = ttk.Button(self.frame_steps, text = 'Initiate', command = lambda: self.timeCompare(self.dailyFileCheck,self.destFileCheck))
        initiateButton.grid(row = 8, column = 0, sticky = 'w')
        
        #path labels
        self.frame_path = ttk.Frame(master)
        self.frame_path.pack()
        dailyPathLabel = ttk.Label(self.frame_steps, text = self.dailyFolderName, textvariable = self.dailyFolderName)
        dailyPathLabel.grid(row = 1, column = 2, rowspan = 1, sticky = 'W')
        dailyPathLabel.config(foreground = 'blue')
        destPathLabel = ttk.Label(self.frame_steps, text = self.destFolderName, textvariable = self.destFolderName)
        destPathLabel.grid(row = 4, column = 2, rowspan = 1, sticky = 'W')
        destPathLabel.config(foreground = 'blue')

        #Timestamp label
        fcTimeTitleLabel = ttk.Label(self.frame_steps, text = 'Last File Check: ')
        fcTimeTitleLabel.grid(row = 7, column = 2, sticky = 'W' )
        fcTimestampLabel = ttk.Label(self.frame_steps, textvariable = self.fcTimestamp)
        fcTimestampLabel.grid(row = 8, column = 2, rowspan = 1, sticky = 'W')
        fcTimestampLabel.config(foreground = 'blue')        


######################## Functions #############################        
        
#Daily folder Browse Window        
    def selectDailyFolder(self):
        self.dailyFileCheck = filedialog.askdirectory(initialdir = "D:\Documents", title = "Select your Daily Folder") #opens dialog box in Documents folder
        self.dailyFolderName.set(self.dailyFileCheck)
        print (self.dailyFileCheck)
        print (self.dailyFolderName.get())
        
#Destination folder Browse Window        
    def selectDestFolder(self):
        self.destFileCheck = filedialog.askdirectory(initialdir = "D:\Documents", title = "Select your Destination Folder") #opens dialog box in Documents folder
        self.destFolderName.set(self.destFileCheck)
        print (self.destFileCheck)
        print (self.destFolderName.get())


#Gets the file's modified time then time 24 hours ago
#Finds each file's path
#And if the file's extension = .txt and modified time is larger than 24 hours ago
#It copies the file to destination folder
    def timeCompare(self, dailyFileCheck, destFileCheck):
        print ('hello {}'.format(dailyFileCheck)) #checks to see if the daily folder name is passing to this function
        print ('hello {}'.format(destFileCheck)) #checks to see if the dest folder name is passing to this function
        print ()
        currentTime = datetime.now() #gives us the current time
        time24hoursAgo = currentTime - timedelta(hours = 24) #finds the time 24 hours from current time
        for f in os.listdir(dailyFileCheck): #listdir lists each file in the directory
            files = os.path.realpath(os.path.join(dailyFileCheck,f)) #shows the file's path then joins the file's path and the directory's paths.  This provides the datetime with the entire file's path
            if files.endswith('.txt'):
                fileSrcModifiedTime = datetime.fromtimestamp(os.path.getmtime(files)) #gives us each file's modified time
                if fileSrcModifiedTime > time24hoursAgo: #if file's modified time is greater than 24 hours old copy file to destination folder
                    print (files, "copied to: ", destFileCheck)
                    shutil.copy(files,destFileCheck) #copys file to destination
                    
                else:
                    print (files, "not copied")
        self.fileCheckdb() #inserts timestamp into db table                  

    #inserts timestamps to db
    def fileCheckdb(self):
        self.db = sqlite3.connect('test.db')
        print('Opened Timestamp database successfully!')
        self.db.execute("INSERT INTO fcRuns (fcTime) VALUES (datetime(CURRENT_TIMESTAMP, 'localtime'))")
        print('Timestamp inserted')
        self.db.commit()
        self.cursor = self.db.execute('SELECT fcTime FROM fcRuns ORDER BY ID DESC LIMIT 1')
        for row in self.cursor:
            print ('Last File Check: ',row)
            self.fcClock = self.fcTimestamp.set(row)
            print ('adslkfjlsadf', row)
            
        self.db.close()
        print ('Database closed')  


############################ MAIN ################################

def main():
    
    root = Tk() #needed for tkinter
    root.wm_title("File Check") #sets the window title
    root.minsize(400, 280) #sets minimum size the window can be
    filecheck = FileCheck(root) #sets the class up with root from tkinter
    root.mainloop() #needed for tkinter


if __name__ == '__main__' :
    main() #runs the main function which runs the class and functions
    print ('main has run')
    
    

