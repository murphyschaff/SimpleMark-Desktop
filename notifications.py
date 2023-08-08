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
'''
def runNotif(list, length, timeZone, notifTimes):

    mark = list.getHead()
    listName = list.getName()
    currentTime = time.time()
    currentTime = DateTime(currentTime, timeZone)

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
            send = checkRemindTime(deadline.timeTime(), notifTimes, currentTime, prio)
            print(send)
            if send is True:
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
    Returns: boolean value (true if should be sent, false if not
    
    deadline: time value of mark's deadline
    notifLength: list of reminder lengths (from config file)
    currentTime: current time of the system
    prio: int priority of the mark 
    '''
def checkRemindTime(deadline, notifLength, currentTime, prio):

    sendRemind = False
    # Runs once for each level in prio, sends one notification if within time frame
    for i in range(prio):
        check = float(notifLength[i])
        check = deadline - check

        if currentTime >= check:
            sendRemind = True

    return sendRemind