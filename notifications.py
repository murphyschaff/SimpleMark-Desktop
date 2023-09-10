from windowstoast import Toast
import time
import datetime
from datetime import datetime
import os
from listmarkclass import *

'''
Checks if mark needs to send notification
Returns: Boolean if all notifications have been run

list: list object of list to check for notificaitons
length: length of list (simplicity purposes)
timeZone: Current time zone, based from config file
notifTimes: List that specifies how frequently (in seconds) to notify for a mark 
runAlready: Boolean list to check if the notif had been run already since opening
'''
def runNotif(list, length, timeZone, notifTimes, runAlready):

    mark = list.getHead()
    listName = list.getName()
    currentTime = datetime.now()

    #Runs for each item in the list
    for i in range(length):
        prio = mark.getPrio()
        deadline = mark.getDeadline()
        #print(runAlready)
        #If the deadline is after the current time, the final notification pops
        if deadline <= currentTime:
            if runAlready[i * 5] == False:
                notif = Toast("SimpleMark", "Mark", ActivationType="protocol", Duration="long")
                cwd = os.getcwd()
                logo = cwd + "\\logo.png"
                #notif.add_image("logo")
                notif.add_text("Mark Deadline Reached")
                notif.add_text("{} has reached deadline from list {}".format(mark.getName(), list.getName()))
                notif.show()
                for x in range(4):
                    runAlready[(i * 5) + x] = True
        else:
            #Reminder notification
            currentRunAlready = []
            #Adds the boolean values for the current prio level to another list
            for x in range(5):
                currentRunAlready.append(runAlready[(i * 5) + x])
            send = checkRemindTime(deadline, notifTimes, prio, currentRunAlready, currentTime)
            if send[0] is True:
                runAlready[(i*5) + send[1]] = True
                notif = Toast("SimpleMark", "Mark", ActivationType="protocol", Duration="long")
                cwd = os.getcwd()
                logo = cwd + "\\logo.png"
                # notif.add_image("logo")
                notif.add_text("Mark Deadline Reminder")
                notif.add_text(
                    "{} with deadline of {} is approaching from {} ".format(mark.getName(), deadline,
                                                                                 listName))
                notif.show()

        mark = mark.getNext()

    stopNotif = True
    #checks and sees if another notification still needs to be run, stops progress if so
    for i in range(len(runAlready)):
        if runAlready[i] == False:
            stopNotif = False
    return stopNotif

'''
Checks if reminder notification should be sent
Returns: List of boolean and int value, i0: if notif should be sent, i1: index of runAlready to update
    
deadline: time value of mark's deadline
notifLength: list of reminder lengths (from config file)
prio: int priority of the mark
runAlready: Boolean list if the notif for that prio has run already
currentTime: Datetime object representing the current time
'''
def checkRemindTime(deadline, notifLength, prio, runAlready, currentTime):

    sendRemind = False
    prio = int(prio)
    #Gets the time values from the deadline datetime obejct, sets to integer
    deadyr = deadline.strftime('%y')
    deadyr = int(deadyr)
    deadmn = deadline.strftime('%m')
    deadmn = int(deadmn)
    deaddy = deadline.strftime('%d')
    deaddy = int(deaddy)
    deadhr = deadline.strftime('%H')
    deadhr = int(deadhr)
    deadmin = deadline.strftime('%M')
    deadmin = int(deadmin)
    difmin = 0
    difhr = 0
    difdy = 0
    difference = []
    #Uses the notif length list to find the difference between the deadline and notif time
    for i in range(len(notifLength)):
        days = 0
        hours = 0
        mins = 0
        sec = 0
        checkTime = notifLength[i]
        #finding how many days, hours, mins, and seconds each notif time is. And finds difference
        if checkTime > 60:
            mins = checkTime / 60
            sec = checkTime % 60
            if mins > 60:
                hours = mins / 60
                mins = mins % 60
                if deadmn - mins < 0:
                    difmin = int((deadmn - mins) % 60)
                    hours = hours + 1
                else:
                    difmin = int(mins)
                if hours > 24:
                    days = hours / 60
                    hours = hours % 60
                    if deadhr - hours < 0:
                        difhr = int((deadhr - hours) % 24)
                        days = days + 1
                    else:
                        difhr = int(hours)
        days = int(days)
        hours = int(hours)
        mins = int(mins)
        sec = int(sec)
        #print('{}: {} {} {} {} {} {}'.format(checkTime, deadyr, deadmn, deaddy - days, difhr, difmin, sec))
        #differences added to datetime object, and added to list
        notifDatetime = datetime(deadyr, deadmn, deaddy - days, difhr, difmin, sec)
        difference.append(notifDatetime)

    run = True
    i = 0
    #Checks and sees if the notifications need to be run, if the deadline is greater than remind time

    while run:
        if currentTime <= difference[i] and not runAlready[i]:
            runAlready[i] = True
            sendRemind = True
            run = False
        else:
            i = i + 1
        if i >= len(difference):
            run = False

    return [sendRemind, i]
