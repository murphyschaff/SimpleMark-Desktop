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
BUTTON FUNCTIONS
'''
def addList(window, file, listFrame):
    #Checks if file opened is a file and is a simple mark file
    if os.path.exists(file) and os.path.isfile(file):
        list = openList(file)
        if list is not None:
            print("Opened list from: {}".format(file))
            name = list.getName()
            window.title("SimpleMark: {}".format(name))

            listString = ""
            mark = list.getHead()
            #clears any previous data from the list
            clearFrame(listFrame)
            #lists every item in the list

            for i in range(list.getLength()):
                listString = listString + mark.getName() + ": \n"
                mark = mark.getNext()

            listLabel = tk.Label(
                master=listFrame,
                text=listString,
                width=30
            )
            listLabel.pack()

            '''
            List Attribute Buttons
            '''
            addItemButton = tk.Button(
                master=listFrame,
                text="Add Item",
                width=20,
                height=1,
                bg="black",
                fg='white',
                command=lambda: addItem()
            )

            removeItemButton = tk.Button(
                master=listFrame,
                text="Remove Item",
                width=20,
                height=1,
                bg="black",
                fg='white',
                command=lambda: removeItem()
            )

            removeListButton = tk.Button(
                master=listFrame,
                text="Delete List",
                width=20,
                height=1,
                bg="black",
                fg='white',
                command=lambda: removeList(list)
            )
            editMarkButton = tk.Button(
                master=listFrame,
                text="Edit Mark Information",
                width=20,
                height=1,
                bg="black",
                fg='white',
                command=lambda: editMark(markEntry.get())
            )
            #Information Text Box
            markEntryLabel = tk.Label(master=listFrame, text="Add name of object to edit/delete")
            markEntry = tk.Entry(
                master=listFrame,
                width=50
            )
            #packing all other buttons and lables
            markEntryLabel.pack()
            markEntry.pack()
            addItemButton.pack()
            removeItemButton.pack()
            editMarkButton.pack()
            removeListButton.pack()


        else:
            tkinter.messagebox.showerror(title="SimpleMark",
                                         message="Not a Simple Mark List File. Please open a Simple Mark List.")
    else:
        tkinter.messagebox.showerror(title="SimpleMark", message="Please open a valid file.")

'''
Clears the frame that is sent to the function of objects
frame: tk frame to have objects removed
'''
def clearFrame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
        print("object destroyed")

'''
creates window to add item to the list
'''
def addItem():
    print("add ran")

'''
removes item from list
'''
def removeItem():
    print("remove ran")
'''
deletes list
'''
def removeList(list):

    print("remove list ran")


'''
Allows for edits to be made to each mark
'''
def editMark(entry):
    print(entry)


'''
main
'''
configData = openConfig()
list = ""
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
    height=5
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

listFrame = tk.Frame()

openButton = tk.Button(
    master=openFrame,
    text="Open List",
    width=20,
    height=1,
    bg="black",
    fg='white',
    command=lambda: addList(window, openEntry.get(), listFrame)
)

openButton.pack()
listFrame.pack()
window.mainloop()
