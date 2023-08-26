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
'''
Creates a new list
window: Tk object of main window
listFrame: Tk frame object of the list frame
'''
def createList(window, createFrame, listFrame):

    deleteFrame(listFrame)

    createLabel = tk.Label(master=createFrame, text="Create New List:")
    createLabel.pack()

    #Label creation
    listNameLabel = tk.Label(master=createFrame, text="List Name")
    markLabel = tk.Label(master=createFrame, text="Mark Information")
    markNameLabel = tk.Label(master=createFrame, text="Mark Name")
    markDetailsLabel = tk.Label(master=createFrame, text="Details")
    markDeadlineLabel = tk.Label(master=createFrame, text="Deadline")
    markPrioLabel = tk.Label(master=createFrame, text="Priority")
    markColorLabel = tk.Label(master=createFrame, text="color")

    # creation of text boxes
    listNameBox = tk.Entry(master=createFrame, width=30)
    nameBox = tk.Entry(master=createFrame, width=30)
    descriptionBox = tk.Entry(master=createFrame, width=30)
    deadlineBox = tk.Entry(master=createFrame, width=30)
    colorBox = tk.Entry(master=createFrame, width=30)
    # prio option menu
    options = [1, 2, 3, 4, 5]
    prioType = IntVar()
    prioType.set(1)
    prioBox = OptionMenu(createFrame, prioType, *options)

    #Button creation
    saveListButton = tk.Button(
        master=createFrame,
        text="Save List",
        width=20,
        height=1,
        bg="black",
        fg='white',
        command=lambda: saveAndOpenList(window, createFrame, prioType)
    )

    cancelButton = tk.Button(
        master=createFrame,
        text="Cancel",
        width=20,
        height=1,
        bg="black",
        fg='white',
        command=lambda: deleteFrame(createFrame)
    )

    #adding objects to frame
    listNameLabel.pack()
    listNameBox.pack()
    markNameLabel.pack()
    nameBox.pack()
    markDetailsLabel.pack()
    descriptionBox.pack()
    markDeadlineLabel.pack()
    deadlineBox.pack()
    markPrioLabel.pack()
    prioBox.pack()
    markColorLabel.pack()
    colorBox.pack()
    saveListButton.pack()
    cancelButton.pack()

'''
Updates the List on the page
windowInfo: List object containing the window, file, and listFrame information
'''
def updateList(windowInfo):

    listFrame = tk.Frame()
    listFrame.pack()

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
        command=lambda: editMark(None, list, 0, windowInfo)
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
        command=lambda: deleteList(list, windowInfo[1])
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
        changeType = "Add"
        showFrame = True
    else:
        changeType ='Edit'
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
                tk.messagebox.showerror(title="SimpleMark", message="Mark {} not found in list {}. Try again"
                                    .format(searchMarkName, list.getName()))


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
Saves and opens list
frame: createFrame that holds all objects
prioType: Priority from createFrame
'''
def saveAndOpenList(window, frame, prioType):
    # starts at index 8
    objects = frame.winfo_children()
    listName = objects[8]
    markName = objects[9]
    markDetails = objects[10]
    markDeadline = objects[11]
    markPrio = int(prioType.get())
    markColor = objects[12]

    listName = listName.get()
    markName = markName.get()
    markDetails = markDetails.get()
    markDeadline = markDeadline.get()
    markColor = markColor.get()

    if isfloat(markDeadline):
        mark = Mark(markName, markDetails, markDeadline, markPrio, markColor)
        list = List(listName, mark)
        file = saveList(list)

        openListFromFile(window, file, listFrame, frame)
        deleteFrame(frame)

    else:
        tk.messagebox.showerror(title='SimpleMark', message="Please enter a number for deadline")


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
Deletes list and file from computer
list: List object to be deleted
windowInfo: information to updateList
'''
def deleteList(list, file):

    check1 = tk.messagebox.askyesno(title="SimpleMark", message="Are you sure you want to remove list '{}'?"
                                    .format(list.getName()))
    if check1:
        check2 = tk.messagebox.askyesno(title="SimpleMark",message="Are you really sure?")
        if check2:
            print("deleted")


'''
Updates the list after a change was made
list: List object needed to be updated
frame: Tk frame editMarkClass
'''
def openListFromFile(window, file, listFrame, createFrame):

    deleteFrame(createFrame)

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
    name = objects[6].get()
    details = objects[7].get()
    deadline = objects[8].get()
    color = objects[9].get()
    prio = int(prioType.get())

    if isfloat(deadline):
        deleteFrame(frame)
        deadline = float(deadline)
        # creating new mark if adding, editing if edit
        if option == 0:
            mark = Mark(name, details, deadline, prio, color)
            list.add(mark)
            saveList(list)

            updateList(windowInfo)
        else:

            mark.changeName(name)
            mark.changeDetails(details)
            mark.changeDeadline(deadline)
            mark.changePriority(prio)
            mark.changeColor(color)

            updateList(windowInfo)
    else:
        tk.messagebox.showerror(title="SimpleMark", message="Please enter a number for a deadline")




'''
removes item from list
markName: String name of mark to be removed
list: List object of mark to remove
windowInfo: stuff needed to run updateList
'''
def removeItem(markName, list, windowInfo):
    mark = list.findMark(markName)
    if mark != None:
        check = tk.messagebox.askokcancel(title="SimpleMark", message="This will remove mark '{}' from list '{}'. Are you sure?"
                                   .format(mark.getName(), list.getName()))
        #if user clicks ok, the item is removed from the list and the lsit is saved
        if check:
            list.remove(mark)
            saveList(list)
            updateList(windowInfo)
    else:
        if markName == '':
            tk.messagebox.showerror(title="SimpleMark", message="Please enter the name of a mark in the list")
        else:
            tk.messagebox.showerror(title="SimpleMark", message="Mark {} not found in list {}".format(markName,
                                                                                                      list.getName()))

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
         return False
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
createFrame = tk.Frame()

openButton = tk.Button(
    master=openFrame,
    text="Open List",
    width=20,
    height=1,
    bg="black",
    fg='white',
    command=lambda: openListFromFile(window, openEntry.get(), listFrame, createFrame)
)

createButton = tk.Button(
    master=openFrame,
    text="Create New List",
    width=20,
    height=1,
    bg="black",
    fg='white',
    command=lambda: createList(window, createFrame, listFrame)
)

createButton.pack()
openButton.pack()
listFrame.pack()
createFrame.pack()
window.mainloop()
