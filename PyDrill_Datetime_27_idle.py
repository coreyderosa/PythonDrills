#Corey DeRosa
#
#Python Course- Item 58 of 64
#
#Datetime-Python 2.7- IDLE

from datetime import datetime
import time

def currentTime():
    print 'The current time at HQ is: ',time.strftime('%A, %B %d, %Y %I:%M%p %Z')


#def nycTime():
    #print 'The current time at at our NYC branch is: ',time.strftime('%a, %b %d %Y %H:%M')



#def londonTime():

currentTime()
