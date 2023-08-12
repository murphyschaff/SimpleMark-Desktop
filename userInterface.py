import os
import tkinter.messagebox
from listmarkclass import *
from files import *
from notifications import *
import tkinter as tk
'''
~~~~~SIMPLEMARK v1~~~~~

Created by Murphy Schaff
'''

'''
PAGES
'''
def listPage():

    destination = openEntry.get()
    #checking if the list exists
    if os.path.exists(destination) and os.path.isfile(destination):
        list = openList(destination)
        listWindow = tk.Tk()
        listWindow.title('SimpleMark List:{}'.format(list.getName()))

        listButtonFrame = tk.Frame(master=listWindow)
        listButtonFrame.pack()
        listButtonAdd = tk.Button(
            master=listButtonFrame,
            text="Add Item",
            command=addItem
        )
        listButtonAdd.pack()
        listButtonRemoveList = tk.Button(
            master=listButtonFrame,
            text="Delete List",
            command=removeList(list)
        )
        listButtonRemoveList.pack()

        items = list.getLength()
        mark = list.getHead()

        for i in range(items):
            markFrame = tk.Frame(master=listWindow)

            markName = tk.Label(master=markFrame,text="{}".format(mark.getName()))
            markName.pack()

            markDeadline = tk.Label(master=markFrame, text="{}".format(mark.getDeadline()))
            markDeadline.pack()

            mark = mark.getNext()

        listWindow.mainloop()
    else:
        tkinter.messagebox.showerror(title="SimpleMark", message="File at destination does not exist")

'''
creates window to add item to the list
'''
def addItem():
    print("ran")


'''
deletes list
'''
def removeList(list):

    print("also ran")



'''
main
'''
configData = openConfig()


if configData != None:
    #open previously known list
    list = openList(configData[1])

    notifTimes = [configData[2], configData[3], configData[4], configData[5], configData[6]]
    print(configData[0])

    #runNotif(list, list.getLength(), configData[0], notifTimes)

    list.list()
else:
    print("Failed to load SimpleMark. Configuration file not found.")
    tkinter.messagebox.showerror(title="SimpleMark", message=
                                       "Failed to load SimpleMark. Configuration file not found.")
window = tk.Tk()
window.title("SimpleMark")
greeting = tk.Label(
    text="Welcome to SimpleMark",
    width=30,
    height=10
)
greeting.pack()

openFrame = tk.Frame()
openFrame.pack()

openLabel = tk.Label(
    master=openFrame,
    text="Open List"
)
openEntry = tk.Entry(width=50)
path = str(configData[1])
openEntry.insert(index=0, string=path)
openEntry.pack()

openButton = tk.Button(
    master=openFrame,
    text="Open List",
    width=20,
    height=1,
    bg="black",
    fg='white',
    command=listPage
)
openButton.pack()

window.mainloop()



