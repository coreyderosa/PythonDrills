#Corey DeRosa
#
#Python Course- Item 58 of 64
#
#Datetime-Python 2.7- IDLE

from datetime import datetime
import time
from pytz import timezone
import pytz

#Determines times for 3 branches with long time format
##def currentTime():
##    timeFormat = '%A, %B %d, %Y %I:%M%p %Z'    
##    print 'The current time at HQ is: ',time.strftime(timeFormat)
##
##def nycTime():
##    est = datetime.now(timezone('US/Eastern'))
##    timeFormat = '%A, %B %d, %Y %I:%M%p %Z'
##    nycClosed = est.strftime(timeFormat)
##    print 'The current time at our NYC branch is: ',est.strftime(timeFormat)
##    print nycClosed
##    
##def londonTime():
##    londonTZ = datetime.now(timezone('Europe/London'))
##    timeFormat = '%A, %B %d, %Y %I:%M%p %Z'
##    print 'The current time at our London branch is: ',londonTZ.strftime(timeFormat)

#Determines Portland Time
def currentTime(): #current
    pst = datetime.now(timezone('US/Pacific'))
    timeFormat = '%I:%M'
    pTime = pst.strftime(timeFormat)
    print 'The current time at HQ in Portland is: ',pst.strftime(timeFormat)
    print pTime

#Determine NYC Time
def nycTime():
    est = datetime.now(timezone('US/Eastern'))
    timeFormat = '%H:%M'
    nTime = est.strftime(timeFormat)
    print 'The current time at our NYC branch is: ',est.strftime(timeFormat)
    print nTime

#Determine London Time
def londonTime(): 
    londonTZ = datetime.now(timezone('Europe/London'))
    timeFormat = '%H:%M'
    lTime = londonTZ.strftime(timeFormat)
    print 'The current time at our London branch is: ',londonTZ.strftime(timeFormat)    
    print lTime
#Determines if branches are open or closed
def officesClosed():
    timeLongFormat = '%I:%M%p %Z' #returns 10:00PM TimeZone
    timeShortFormat = '%H' #returns 10
    est = datetime.now(timezone('US/Eastern')) #Eastern time zone current time
    nTime = est.strftime(timeLongFormat) #Eastern time in string format 
    lst = datetime.now(timezone('Europe/London')) #London time zone current time
    lTime = lst.strftime(timeLongFormat) #London time in string format
    pst = datetime.now(timezone('US/Pacific')) #Pacific time zone current time
    pTime = pst.strftime(timeLongFormat) #Pacific time in string format
    mst = datetime.now(timezone('US/Mountain'))
    mTime = mst.strftime(timeLongFormat)

    #NYC branch
    if est.hour >= 21 or est.hour < 9:
        print 'The NYC branch is closed since it is', nTime
    else:
        print 'The NYC branch is open since it is', nTime

    #London branch
    if lst.hour >= 21 or lst.hour < 9:
        print 'The London branch is closed since it is', lTime
    else:
        print 'The London branch is open since it is', lTime
        
    #Portland (HQ) branch
    if pst.hour >= 21 or pst.hour < 9:
        print 'The Portland branch is closed since it is', pTime
    else:
        print 'The Portland branch is open since it is', pTime

    #Colorado branch- used for testing since I live in Mountain TimeZone
    if mst.hour >= 21 or mst.hour < 9:
        print 'The Colorado branch is closed since it is', mTime
    else:
        print 'The Colorado branch is open since it is', mTime        
###################################################
##currentTime()
##nycTime()
##londonTime()
officesClosed()
