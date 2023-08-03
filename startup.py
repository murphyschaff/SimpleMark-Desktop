import os
from listmarkclass import *
from files import *


'''
~~~~~SIMPLEMARK v1~~~~~

Created by Murphy Schaff
'''

#Load data from config file
configData = openConfig()

#open previously known list
list = openList(configData[0])

list.list()