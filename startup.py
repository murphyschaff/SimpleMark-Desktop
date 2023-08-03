import os
import tkinter.messagebox
from listmarkclass import *
from files import *


'''
~~~~~SIMPLEMARK v1~~~~~

Created by Murphy Schaff
'''

#Load data from config file
configData = openConfig()


if configData != None:
    #open previously known list
    list = openList(configData[0])

    list.list()
else:
    print("Failed to load SimpleMark. Configuration file not found.")
    tkinter.messagebox.showerror(title="SimpleMark", message=
                                       "Failed to load SimpleMark. Configuration file not found.")
