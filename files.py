import os
import re
from listmarkclass import *

print(os.getcwd())

'''
Saves List to ListData file
listHead: Mark object head of list
name: string object of name of list
length: integer value of the length of the list
'''
def saveList(listHead, name, length):
    cwd = os.getcwd()
    directory = cwd + "\\ListData"

    if not os.path.exists(directory):
        os.mkdir(cwd + "\\ListData")

    file = open(directory + "\\" + name + ".txt", 'w')
    #initial list information
    file.write("{}\n{}\n".format(name, length))
    mark = listHead

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

        # finding and creating the head mark
        data = file.readline()
        regex = re.compile(r'\w+')
        output = regex.findall(data)

        markName = output[0]
        markDetails = output[1]
        markDeadline = output[2]
        markPrio = output[3]
        markColor = output[4]

        # initiating the head mark and list to return
        headMark = Mark(markName, markDetails, markDeadline, markPrio, markColor)

        list = List(listName, headMark)

        # doing the same for all other marks in the list
        for i in range(length - 1):
            data = file.readline()
            output = regex.findall(data)

            markName = output[0]
            markDetails = output[1]
            markDeadline = output[2]
            markPrio = output[3]
            markColor = output[4]

            newMark = Mark(markName, markDetails, markDeadline, markPrio, markColor)

            list.add(newMark)

        return list













