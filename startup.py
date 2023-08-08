import os
import tkinter.messagebox
from listmarkclass import *
from files import *
from notifications import *


'''
~~~~~SIMPLEMARK v1~~~~~

Created by Murphy Schaff
'''

#Load data from config file
configData = openConfig()


if configData != None:
    #open previously known list
    list = openList(configData[1])

    notifTimes = [configData[2], configData[3], configData[4], configData[5], configData[6]]
    print(configData[0])

    runNotif(list, list.getLength(), configData[0], notifTimes)

    list.list()
else:
    print("Failed to load SimpleMark. Configuration file not found.")
    tkinter.messagebox.showerror(title="SimpleMark", message=
                                       "Failed to load SimpleMark. Configuration file not found.")
