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
    print(currentTime)
    print(length)

    #Runs for each item in the list
    for i in range(length):
        prio = mark.getPrio()
        deadline = mark.getDeadline()
        print(deadline)
        deadline = DateTime(deadline, timeZone)
        print(mark.getName())

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
            '''
            Sends periodic reminders based on what level of priority the mark is
            times can be changed based on config values
            level 5 sends reminders at each interval, level 1 only at the first and lowest interval
            '''
            if prio == 1:
                checkTime = deadline - notifTimes[0]
                if checkTime >= currentTime:
                    sendRemindNotif(mark, listName)
            elif prio == 2:
                time1 = deadline - notifTimes[0]
                time2 = deadline - notifTimes[1]

                if checkTime >= time1:
                    sendRemindNotif(mark, listName)
                elif checkTime >= time2:
                    sendRemindNotif(mark, listName)
            elif prio == 3:
                time1 = deadline - notifTimes[0]
                time2 = deadline - notifTimes[1]
                time3 = deadline - notifTimes[2]

                if checkTime >= time1:
                    sendRemindNotif(mark, listName)
                elif checkTime >= time2:
                    sendRemindNotif(mark, listName)
                elif checkTime >= time3:
                    sendRemindNotif(mark, listName)
            elif prio == 4:
                time1 = deadline - notifTimes[0]
                time2 = deadline - notifTimes[1]
                time3 = deadline - notifTimes[2]
                time4 = deadline - notifTimes[3]

                if checkTime >= time1:
                    sendRemindNotif(mark, listName)
                elif checkTime >= time2:
                    sendRemindNotif(mark, listName)
                elif checkTime >= time3:
                    sendRemindNotif(mark, listName)
                elif checkTime >= time4:
                    sendRemindNotif(mark, listName)
            else:
                time1 = deadline - notifTimes[0]
                time2 = deadline - notifTimes[1]
                time3 = deadline - notifTimes[2]
                time4 = deadline - notifTimes[3]
                time5 = deadline - notifTimes[4]

                if checkTime >= time1:
                    sendRemindNotif(mark, listName)
                elif checkTime >= time2:
                    sendRemindNotif(mark, listName)
                elif checkTime >= time3:
                    sendRemindNotif(mark, listName)
                elif checkTime >= time4:
                    sendRemindNotif(mark, listName)
                elif checkTime >= time5:
                    sendRemindNotif(mark, listName)

        mark = mark.getNext()

'''
Formats and sends the reminder notifications for marks
mark: mark object to be reminded of
listName: name of the list the mark is a member of
'''
def sendRemindNotif(mark, listName):
    notif = Toast("SimpleMark", "Mark", ActivationType="protocol", Duration="long")
    cwd = os.getcwd()
    logo = cwd + "\\logo.png"
    # notif.add_image("logo")
    notif.add_text("Mark Deadline Reminder")
    notif.add_text("{} with deadline of {} is approaching from list {} ".format(mark.getName(), mark.getDeadline(),
                                                                                listName))
