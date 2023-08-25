import os
import tkinter.messagebox
from listmarkclass import *
from files import *
from notifications import *
import tkinter as tk
from tkinter import *
'''
~~~~~SIMPLEMARK v1~~~~~

Created by Murphy Schaff
'''
'''
PAGES
'''
def updateList(windowInfo):

    listString = ""
    mark = list.getHead()
    #clears any previous data from the list
    clearFrame(listFrame)
    #lists every item in the list

    for i in range(list.getLength()):
        listString = listString + mark.getName() + ": {}, {}, {}\n".format(mark.getDetails(),
                                                                                   mark.getDeadline(),
                                                                                   mark.getPrio())
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
        command=lambda: editMark("", list, 0)
    )

    removeItemButton = tk.Button(
        master=listFrame,
        text="Remove Item",
        width=20,
        height=1,
        bg="black",
        fg='white',
        command=lambda: removeItem(markEntry.get(), list, windowInfo)
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
        command=lambda: editMark(markEntry.get(), list, 1, windowInfo)
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


'''
Allows for changes to be made to specific marks
searchMarkName: String of the name of the mark to be edited
list: List object to be searched/added
option: Int value (0,1) of mark to be added/edited
'''
def editMark(searchMarkName, list, option, windowInfo):

    #basic variable creation for mark options
    name = ''
    details =''
    deadline = 0.0
    prio = 0
    color =''
    changeType = ''
    #changes edit/add mark button text
    buttonText ='Add Mark'
    #for option 1, if the mark is found in list it will show. otherwise it wont
    showFrame = False
    mark = None

    # 0:add new mark, 1==edit existing mark
    if option == 0:
        changeType = "add"
        showFrame = True
    else:
        changeType ='edit'
        mark = list.findMark(searchMarkName)
        #checks if mark exists, and if a query was entered
        if mark is not None:
            name = mark.getName()
            details = mark.getDetails()
            deadline = mark.getDeadline()
            color = mark.getColor()
            buttonText = 'Save Changes'
            showFrame = True
        else:
            if searchMarkName == '':
                tk.messagebox.showerror(title="SimpleMark", message="Please enter the name of a mark to edit")
            else:
                tk.messagebox.showerror(title="SimpleMark", message="Mark not found in list {}. Try again"
                                    .format(list.getName()))


    editMarkFrame = tk.Frame()
    editMarkFrame.pack()

    #creation of labels
    titleLabel = tk.Label(master=editMarkFrame, text="{} Mark: {}".format(changeType, name))
    nameLabel = tk.Label(master=editMarkFrame,text="Mark Name")
    descriptionLabel = tk.Label(master=editMarkFrame, text="Mark Description")
    deadlineLabel = tk.Label(master=editMarkFrame, text="Mark Deadline")
    prioLabel = tk.Label(master=editMarkFrame, text="Mark Priority")
    colorLabel = tk.Label(master=editMarkFrame, text="Mark Color")

    #creation of text boxes
    nameBox = tk.Entry(master=editMarkFrame, width=30)
    descriptionBox = tk.Entry(master=editMarkFrame, width=30)
    deadlineBox = tk.Entry(master=editMarkFrame, width=30)
    colorBox = tk.Entry(master=editMarkFrame, width=30)
    #prio option menu
    options = [1,2,3,4,5]
    prioType = IntVar()
    if option == 0:
        prioType.set(1)
    else:
        if showFrame:
            prioType.set(mark.getPrio())
    prioDrop = OptionMenu(editMarkFrame,prioType, *options)

    #adding details if the mark already exists
    if option ==1:

        nameBox.insert(0, "{}".format(name))
        descriptionBox.insert(0, "{}".format(details))
        deadlineBox.insert(0, "{}".format(deadline))
        colorBox.insert(0, "{}".format(color))

    #button definitions
    saveMarkButton = tk.Button(
        master=editMarkFrame,
        text='{}'.format(buttonText),
        width=20,
        height=1,
        bg="black",
        fg='white',
        command=lambda: addMark(mark, list, option, editMarkFrame, prioType, windowInfo)
    )

    cancelMarkEditButton = tk.Button(
        master=editMarkFrame,
        text="Cancel",
        width=20,
        height=1,
        bg="black",
        fg='white',
        command=lambda: deleteFrame(editMarkFrame)
    )

    if showFrame:
    #packing all items
        titleLabel.pack()
        nameLabel.pack()
        nameBox.pack()
        descriptionLabel.pack()
        descriptionBox.pack()
        deadlineLabel.pack()
        deadlineBox.pack()
        prioLabel.pack()
        prioDrop.pack()
        colorLabel.pack()
        colorBox.pack()
        saveMarkButton.pack()
        cancelMarkEditButton.pack()
    else:
        deleteFrame(editMarkFrame)






'''
BUTTON FUNCTIONS
'''
'''
Removes frame from screen
frame: Tk frame object to be deleted
'''
def deleteFrame(frame):
    frame.destroy()
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
mark: Mark object to be added/edited
list: List object for the mark in question
option: Int value (0,1) 0: add new mark, 1: save changes to mark
frame: Tk editMarkClass frame
prioType: data inside option box
'''
def addMark(mark, list, option, frame, prioType, windowInfo):
    #finding information from the frame
    objects = frame.winfo_children()
    print(objects)
    name = objects[6].get()
    details = objects[7].get()
    deadline = objects[8].get()
    color = objects[9].get()
    prio = prioType.get()
    deleteFrame(frame)

    #creating new mark if adding, editing if edit
    if option == 0:
        mark = Mark(name, details, deadline, prio, color)
        list.add(mark)

        updateList(list, frame, windowInfo)
    else:

        mark.changeName(name)
        mark.changeDetails(details)
        mark.changeDeadline(float(deadline))
        mark.changePriority(int(prio))
        mark.changeColor(color)

        updateList(windowInfo)



'''
removes item from list
markName: String name of mark to be removed
list: List object of mark to remove
'''
def removeItem(markName, list, windowInfo):
    mark = list.findMark(markName)
    if mark != None:
        check = tk.messagebox.showinfo(title="SimpleMark", message="This will remove mark {} from list {}"
                                   .format(mark.getName(), list.getName()))
    else:
        if markName == '':
            tk.messagebox.showerror(title="SimpleMark", message="Please enter the name of a mark in the list")
        else:
            tk.messagebox.showerror(title="SimpleMark", message="Mark not found in list {}".format(list.getName()))

'''
deletes list
'''
def removeList(list):

    print("remove list ran")

'''
Updates the list after a change was made
list: List object needed to be updated
frame: Tk frame editMarkClass
'''
def openListFromFile(window, file, listFrame):
    if os.path.exists(file) and os.path.isfile(file):
        list = openList(file)
        if list is not None:
            print("Opened list from: {}".format(file))
            name = list.getName()
            window.title("SimpleMark: {}".format(name))
            windowInfo = [window, file, listFrame]

            updateList(windowInfo)
        else:
            tkinter.messagebox.showerror(title="SimpleMark",
                                         message="Not a Simple Mark List File. Please open a Simple Mark List.")
    else:
        tkinter.messagebox.showerror(title="SimpleMark", message="Please open a valid file.")



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
    command=lambda: openListFromFile(window, openEntry.get(), listFrame)
)

openButton.pack()
listFrame.pack()
window.mainloop()
