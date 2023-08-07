from windowstoast import Toast
import time
import os
from listmarkclass import *



'''
Checks if mark needs to send notification
list: list object of list to check for notificaitons
length: length of list (simplicity purposes)
'''
def runNotif(list, length):

    mark = list.getHead()
    currentTime = time.ctime()
    print(currentTime)
    print(length)

    #Runs for each item in the list
    for i in range(length):
        prio = mark.getPrio()
        deadline = mark.getDeadline()
        print(mark.getName())

        #If the deadline is after the current time, the notification pops
        if deadline <= currentTime:
            notif = Toast("SimpleMark", "Mark", ActivationType="protocol", Duration="long")
            cwd = os.getcwd()
            logo = cwd + "/logo.png"
            # notif.add_image("logo")
            notif.add_text("Mark Deadline Reached")
            notif.add_text("{} has reached deadline from list {}".format(mark.getName(), list.getName()))
            notif.show()
        mark = mark.getNext()
