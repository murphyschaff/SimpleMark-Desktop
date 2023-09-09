import os
import re
from listmarkclass import *
from miscFunctions import *
import string

'''
Saves List to ListData file
Returns: File path of location saved to
list: list object to be saved to file
'''
def saveList(list):
    name = list.getName()
    length = list.getLength()
    cwd = os.getcwd()
    directory = cwd + "\\ListData"
    watermark = "SimpleMarkListType"
    #Makes sure that the directory exists before adding file there
    if os.path.exists(directory):
        filePath = directory + "\\" + name + ".txt"

        file = open(filePath, 'w')

        file.write('{}\n{}\n{}\n'.format(watermark, name, length))
        mark = list.getHead()

        for i in range(length):
            name = mark.getName()
            details = mark.getDetails()
            deadline = mark.getDeadline()
            deadline = str(deadline)
            prio = mark.getPrio()
            color = mark.getColor()
            #Keys for encoding
            namek = keyGen(len(name))
            detailsk = keyGen(len(details))
            deadlinek = keyGen(len(deadline))
            priok = keyGen(1)
            colork = keyGen(len(color))
            #finding largest length string
            lengths = [len(name), len(details), len(deadline), 1, len(color)]
            largestLength = lengths[i]
            for i in range(len(lengths)):
                if lengths[i] > largestLength:
                    largestLength = lengths[i]
            #encodes the details for each mark before printing to file
            encodedName = str(len(name)) + ',' + encode(namek, name) + randomstring(largestLength - len(name))
            encodedDetails = str(len(details)) + ',' + encode(detailsk, details) + randomstring(largestLength - len(details))
            encDeadline = str(len(deadline))+ ',' + encode(deadlinek, deadline) + randomstring(largestLength - len(deadline))
            encodedPrio = '1,' + encode(priok, str(prio)) + randomstring(largestLength - 1)
            encodedColor = str(len(color)) + ',' + encode(colork, color) + randomstring(largestLength - len(color))
            print('{} {} {} {} {}'.format(encodedName, encodedDetails, encDeadline, encodedPrio, encodedColor))
            #turning key into text
            namek = str(len(namek)) + ',' + numToStringKey(namek) + randomstring(largestLength - len(namek))
            detailsk = str(len(detailsk))+ ',' + numToStringKey(detailsk) + randomstring(largestLength - len(detailsk))
            deadlinek = str(len(deadlinek)) + ',' + numToStringKey(deadlinek) + randomstring(largestLength - len(deadlinek))
            priok = '1,' + numToStringKey(priok) + randomstring(largestLength - 1)
            colork = str(len(colork)) + ',' + numToStringKey(colork) + randomstring(largestLength - len(colork))

            file.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(encodedName,namek, encodedDetails, detailsk,
                                                                         encDeadline, deadlinek, encodedPrio, priok,
                                                                         encodedColor, colork))
            mark = mark.getNext()

        file.close()
        print("File saved to: {}".format(filePath))
        return filePath

'''
Opens list at specified path
Returns: List object holding list data from loaded file, none if not valid list
path: string location of path
'''
def openList(path):

    if os.path.exists(path) and os.path.isfile(path):
        file = open(path, 'r')

        watermark = file.readline()
        watermark = watermark.strip()
        check = "SimpleMarkListType"

        #Makes sure the object is actually a simple mark list
        if watermark == check:
            listName = file.readline()
            listName = listName.strip()
            #finds length and defines regex to read from file
            length = int(file.readline())
            #finds all information for first mark in list
            name = file.readline()
            namek = file.readline()
            details = file.readline()
            detailsk = file.readline()
            deadline = file.readline()
            deadlinek = file.readline()
            prio = file.readline()
            priok = file.readline()
            color = file.readline()
            colork = file.readline()

            #removing new line character
            name = name.strip()
            namek = namek.strip()
            details = details.strip()
            detailsk = detailsk.strip()
            deadline = deadline.strip()
            deadlinek = deadlinek.strip()
            prio = prio.strip()
            priok = priok.strip()
            color = color.strip()
            colork = colork.strip()

            #finding true values of each line
            name = findString(name)
            namek = findString(namek)
            details = findString(details)
            detailsk = findString(detailsk)
            deadline = findString(deadline)
            deadlinek = findString(deadlinek)
            prio = findString(prio)
            priok = findString(priok)
            color = findString(color)
            colork = findString(colork)
            #decoding message: turning key into numbers
            namek = stringToNumKey(namek)
            detailsk = stringToNumKey(detailsk)
            deadlinek = stringToNumKey(deadlinek)
            priok = stringToNumKey(priok)
            colork = stringToNumKey(colork)

            #decoding actual messages
            name = decrypt(namek, name)
            details = decrypt(detailsk, details)
            deadline = decrypt(deadlinek, deadline)
            deadline = translateDatetime(deadline)
            prio = decrypt(priok, prio)
            color = decrypt(colork, color)

            headMark = Mark(name, details, deadline, int(prio), color)

            list = List(listName, headMark)

            #Adds the rest of the marks in the list
            for i in range(length - 1):
                name = file.readline()
                namek = file.readline()
                details = file.readline()
                detailsk = file.readline()
                deadline = file.readline()
                deadlinek = file.readline()
                prio = file.readline()
                priok = file.readline()
                color = file.readline()
                colork = file.readline()

                # removing new line character
                name = name.strip()
                namek = namek.strip()
                details = details.strip()
                detailsk = detailsk.strip()
                deadline = deadline.strip()
                deadlinek = deadlinek.strip()
                prio = prio.strip()
                priok = priok.strip()
                color = color.strip()
                colork = colork.strip()

                # finding true values of each line
                name = findString(name)
                namek = findString(namek)
                details = findString(details)
                detailsk = findString(detailsk)
                deadline = findString(deadline)
                deadlinek = findString(deadlinek)
                prio = findString(prio)
                priok = findString(priok)
                color = findString(color)
                colork = findString(colork)

                # decoding message: turning key into numbers
                namek = stringToNumKey(namek)
                detailsk = stringToNumKey(detailsk)
                deadlinek = stringToNumKey(deadlinek)
                priok = stringToNumKey(priok)
                colork = stringToNumKey(colork)

                # decoding actual messages
                name = decrypt(namek, name)
                details = decrypt(detailsk, details)
                deadline = decrypt(deadlinek, deadline)
                prio = decrypt(priok, prio)
                color = decrypt(colork, color)

                newMark = Mark(name, details, deadline, int(prio), color)

                list.add(newMark)

            file.close()
            return list

        else:
            return None
    else:
        return None

'''
Opens and reads information from the config file, converts information into an array
Returns: Array with config information or None if not found
'''
def openConfig():
    cwd = os.getcwd()
    directory = cwd + "\\config\\config.txt"

    if os.path.exists(directory) and os.path.isfile(directory):
        data = ['','','','','','','','']
        config = open(directory, 'r')

        #Time Zone
        timeRegex = re.compile(r'TimeZone: (\S+)')
        line = config.readline()
        timeZone = timeRegex.search(line)

        data[0] = timeZone.group(1)

        #previous list
        listRegex = re.compile(r'Previous List: (.*)')
        line = config.readline()
        previousList = listRegex.search(line)

        data[1] = previousList.group(1)

        # Notification timings for priority levels
        #prio 1
        notifRegex = re.compile(r'Notif for prio 1: (\d+)')
        line = config.readline()
        notifNum = notifRegex.search(line)

        data[2] = float(notifNum.group(1))
        #2
        notifRegex = re.compile(r'Notif for prio 2: (\d+)')
        line = config.readline()
        notifNum = notifRegex.search(line)

        data[3] = float(notifNum.group(1))
        #3
        notifRegex = re.compile(r'Notif for prio 3: (\d+)')
        line = config.readline()
        notifNum = notifRegex.search(line)

        data[4] = float(notifNum.group(1))
        #4
        notifRegex = re.compile(r'Notif for prio 4: (\d+)')
        line = config.readline()
        notifNum = notifRegex.search(line)

        data[5] = float(notifNum.group(1))
        #5
        notifRegex = re.compile(r'Notif for prio 5: (\d+)')
        line = config.readline()
        notifNum = notifRegex.search(line)

        data[6] = float(notifNum.group(1))

        #Reminders time
        remindRegex = re.compile(r'Time between reminder check: (\d+)')
        line = config.readline()
        remindNum = remindRegex.search(line)

        data[7] = int(remindNum.group(1))


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

    #Reminders time
    remindersTime = configData[7]
    config.write("Time between reminder check: {}\n".format(remindersTime))

    config.close()
