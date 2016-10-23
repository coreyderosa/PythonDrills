from tkinter import *
from tkinter import ttk as ttk, messagebox, filedialog
from datetime import datetime, timedelta
import os
import time
import shutil
from glob import glob
import sqlite3

import PythonDrill_db_35

def loadGUI(self):
    #Frame for header
    self.frame_header = ttk.Frame(self.master)
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
    headerLabel = ttk.Label(self.master.frame_header, image = self.logo).grid(row = 0, column = 0, columnspan = 2, pady = 5, sticky = 'w')
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

    fcTimeTitleLabel = ttk.Label(self.frame_steps, text = 'Last File Check: ')
    fcTimeTitleLabel.grid(row = 7, column = 2, sticky = 'W' )
    fcTimestampLabel = ttk.Label(self.frame_steps, textvariable = self.fcTimestamp)
    fcTimestampLabel.grid(row = 8, column = 2, rowspan = 1, sticky = 'W')
    fcTimestampLabel.config(foreground = 'blue')        

    PythonDrill_db_35.firstRundb(self)

if __name__ == "__main__":
    pass
