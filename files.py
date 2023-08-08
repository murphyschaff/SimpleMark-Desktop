import os
import re
from listmarkclass import *


'''
Saves List to ListData file

list: list object to be saved to file
'''
def saveList(list):
    name = list.getName()
    length = list.getLength()
    cwd = os.getcwd()
    directory = cwd + "\\ListData"

    if not os.path.exists(directory):
        os.mkdir(cwd + "\\ListData")

    file = open(directory + "\\" + list.getName() + ".txt", 'w')
    #initial list information
    file.write("{}\n{}\n".format(name, length))
    mark = list.getHead()

    run = True
    while run:
        #Writes each mark to the file with string ',*,' between each entry
        file.write("{},&,{},&,{},&,{},&,{}\n".format(
            mark.getName(), mark.getDetails(), mark.getDeadline(),
        mark.getPrio(), mark.getColor())
        )
        if mark.getNext() == None:
            run = False
        else:
            mark = mark.getNext()

    file.close()
    print("File has been saved to: " + directory)

'''
Opens list at specified path
Returns: List object holding list data from loaded file
path: string location of path
'''
def openList(path):

    if os.path.exists(path) and os.path.isfile(path):
        file = open(path, 'r')

        listName = file.readline()
        length = int(file.readline())

        regex = re.compile(r'\w+')
        timeRegex = re.compile(r'[0-9]+\.[0-9]+')
        # getting mark data for the list
        for i in range(length):
            data = file.readline()
            output = regex.findall(data)
            timeOutput = timeRegex.search(data)

            markName = output[0]
            markDetails = output[1]
            #reads deadline values as floating point numbers
            markDeadline = float(timeOutput.group(0))
            markPrio = output[3]
            markColor = output[4]

            #If first mark, creates the list object and adds the first mark as the head of list
            if i == 0:
                headMark = Mark(markName, markDetails, markDeadline, markPrio, markColor)
                list = List(listName, headMark)
            else:
                #Otherwise adds the other marks to the list
                newMark = Mark(markName, markDetails, markDeadline, markPrio, markColor)
                list.add(newMark)
        file.close()
        return list


'''
Opens and reads information from the config file, converts information into an array
Returns: Array with config information or None if not found
'''
def openConfig():
    cwd = os.getcwd()
    directory = cwd + "\\config\\config.txt"

    if os.path.exists(directory) and os.path.isfile(directory):
        data = ['','','','','','','']
        config = open(directory, 'r')

        #Time Zone
        timeRegex = re.compile(r'TimeZone: (\S+)')
        line = config.readline()
        timeZone = timeRegex.search(line)

        data[0] = timeZone.group(1)

        #previous list
        listRegex = re.compile(r'Previous List: (\S+)')
        line = config.readline()
        previousList = listRegex.search(line)

        data[1] = previousList.group(1)

        # Notification timings for priority levels
        #prio 1
        notifRegex = re.compile(r'Notif for prio 1: (\d+)')
        line = config.readline()
        notifNum = notifRegex.search(line)

        data[2] = notifNum.group(1)
        #2
        notifRegex = re.compile(r'Notif for prio 2: (\d+)')
        line = config.readline()
        notifNum = notifRegex.search(line)

        data[3] = notifNum.group(1)
        #3
        notifRegex = re.compile(r'Notif for prio 3: (\d+)')
        line = config.readline()
        notifNum = notifRegex.search(line)

        data[4] = notifNum.group(1)
        #4
        notifRegex = re.compile(r'Notif for prio 4: (\d+)')
        line = config.readline()
        notifNum = notifRegex.search(line)

        data[5] = notifNum.group(1)
        #5
        notifRegex = re.compile(r'Notif for prio 5: (\d+)')
        line = config.readline()
        notifNum = notifRegex.search(line)

        data[6] = notifNum.group(1)


        config.close()
        return data
    else:
        #if config file does not exist, errors out
        return None

'''
Saves configuation data to config file
configData: List that contains all options in the config file
'''
def saveConfig(configData):

    cwd = os.getcwd()
    directory = cwd + "\\config"

    if not os.path.exists(directory):
        os.mkdir(directory)

    config = open(directory + "\\config.txt", 'w')

    #TimeZone
    timeZone = configData[0]
    config.write("TimeZone: {}\n".format(timeZone))

    #Previous list
    listPath = configData[1]
    config.write("Previous List: {}\n".format(listPath))

    #Notification Timings
    #prio 1
    prioNotifTime = configData[2]
    config.write("Notif for prio 1: {}\n".format(prioNotifTime))
    #2
    prioNotifTime = configData[3]
    config.write("Notif for prio 2: {}\n".format(prioNotifTime))
    #3
    prioNotifTime = configData[4]
    config.write("Notif for prio 3: {}\n".format(prioNotifTime))
    #4
    prioNotifTime = configData[5]
    config.write("Notif for prio 4: {}\n".format(prioNotifTime))
    #5
    prioNotifTime = configData[6]
    config.write("Notif for prio 5: {}\n".format(prioNotifTime))

    config.close()











