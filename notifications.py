from windowstoast import Toast
import time
from DateTime import DateTime
import os
from listmarkclass import *



'''
Checks if mark needs to send notification
list: list object of list to check for notificaitons
length: length of list (simplicity purposes)
timeZone: Current time zone, based from config file
notifTimes: List that specifies how frequently (in seconds) to notify for a mark
runAlready: Boolean list to check if the notif had been run already since opening
'''
def runNotif(list, length, timeZone, notifTimes, runAlready):

    mark = list.getHead()
    listName = list.getName()
    currentTime = time.time()
    currentTime = DateTime(currentTime, timeZone)
    print(runAlready)

    #Runs for each item in the list
    for i in range(length):
        prio = mark.getPrio()
        deadline = mark.getDeadline()
        deadline = DateTime(deadline, timeZone)

        #If the deadline is after the current time, the final notification pops
        if deadline <= currentTime:
            notif = Toast("SimpleMark", "Mark", ActivationType="protocol", Duration="long")
            cwd = os.getcwd()
            logo = cwd + "\\logo.png"
            #notif.add_image("logo")
            notif.add_text("Mark Deadline Reached")
            notif.add_text("{} has reached deadline from list {}".format(mark.getName(), list.getName()))
            notif.show()
        else:
            #Reminder notification
            currentRunAlready = []
            currentRunAlready.append([runAlready[(i*5)], runAlready[(i*5)+1], runAlready[(i*5)+2], runAlready[(i*5)+3],
                                      runAlready[(i*5)+4]])
            send = checkRemindTime(deadline.timeTime(), notifTimes, currentTime, prio, currentRunAlready)
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

'''
Checks if reminder notification should be sent
Returns: List of boolean and int value, i0: if notif should be sent, i1: index of runAlready to update
    
deadline: time value of mark's deadline
notifLength: list of reminder lengths (from config file)
currentTime: current time of the system
prio: int priority of the mark
runAlready: Boolean list if the notif for that prio has run already
'''
def checkRemindTime(deadline, notifLength, currentTime, prio, runAlready):

    sendRemind = False
    prio = int(prio)
    run = True
    i = 0
    while run:
        if deadline > notifLength[i] and not runAlready[i]:
            runAlready[i] = True
            sendRemind = True
            run = False
        else:
            i = i + 1
        if i > 4:
            run = False

    return [sendRemind, i]
