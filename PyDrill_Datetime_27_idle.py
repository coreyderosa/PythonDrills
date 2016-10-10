#Corey DeRosa
#
#Python Course- Item 58 of 64
#
#Datetime-Python 2.7- IDLE

from datetime import datetime
import time
from pytz import timezone
import pytz


def currentTime():
    timeFormat = '%A, %B %d, %Y %I:%M%p %Z'    
    print 'The current time at HQ is: ',time.strftime(timeFormat)


def nycTime():
    est = datetime.now(timezone('US/Eastern'))
    timeFormat = '%A, %B %d, %Y %I:%M%p %Z'
    print 'The current time at our NYC branch is: ',est.strftime(timeFormat)
    
def londonTime():
    londonTZ = datetime.now(timezone('Europe/London'))
    timeFormat = '%A, %B %d, %Y %I:%M%p %Z'
    print 'The current time at our London branch is: ',londonTZ.strftime(timeFormat)


currentTime()
nycTime()
londonTime()
