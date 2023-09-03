import os
import tkinter.messagebox
from listmarkclass import *
from files import *
from notifications import *
import tkinter as tk
from tkinter import *
import time
import threading

'''
~~~~~SIMPLEMARK v1~~~~~

Created by Murphy Schaff; 2023
'''

'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
PAGES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

'''
Contains the options to create or open list
window: Tk object of the program
configData: List with configuration data
'''
def mainPage(window):
    mainFrame = tk.Frame()
    mainFrame.pack()
    window.title("SimpleMark")

    greeting = tk.Label(
        master=mainFrame,
        text="Welcome to SimpleMark\nProgram by Murphy Schaff; 2023",
        width=50,
        height=5
    )
    configButton = tk.Button(
        master=mainFrame,
        text='Edit Config',
        width=10,
        height=1,
        command=lambda: editConfig(configData, window, mainFrame)
    )

    configButton.pack()
    greeting.pack()

    openButton = tk.Button(
        master=mainFrame,
        text="Open List",
        width=20,
        height=1,
        bg="black",
        fg='white',
        command=lambda: openListFromFile(window, getPath(dropType.get(), names, paths), mainFrame)
    )

    createButton = tk.Button(
        master=mainFrame,
        text="Create New List",
        width=20,
        height=1,
        bg="black",
        fg='white',
        command=lambda: createList(window, mainFrame)
    )

    # Finding all lists in ListData file.
    cwd = os.getcwd()
    dir = cwd + "\\ListData"
    files = os.listdir(dir)
    names = []
    paths = []

    for i in range(len(files)):
        path = dir + "\\" + files[i]
        if os.path.exists(path) and os.path.isfile(path):
            check = open(path, 'r')
            watermark = check.readline()
            watermark = watermark.strip()
            if watermark == "SimpleMarkListType":
                names.append(files[i])
                paths.append(path)
    dropType = StringVar()

    createButton.pack()
    if len(names) > 0:
        dropType.set(names[0])
        openFileOption = OptionMenu(mainFrame, dropType, *names)
        openFileOption.pack()
        openButton.pack()

'''
Creates a new list
window: Tk object of main window
listFrame: Tk frame object of the list frame
'''
def createList(window, mainFrame):

    deleteFrame(mainFrame, [False])
    window.title("SimpleMark: Create List")

    createFrame = tk.Frame()
    createFrame.pack()

    createLabel = tk.Label(master=createFrame, text="Create New List:", width=50)
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
        command=lambda: deleteFrame(createFrame, [True, window])
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
Allows for viewing and editing of the conifguration file
configData: list that holds all configuration data
window: Tk window object
'''
def editConfig(configData, window, mainFrame):

    deleteFrame(mainFrame, [False])

    configFrame = tk.Frame()
    configFrame.pack()

    #Label Creation
    configLabel = tk.Label(master=configFrame, text="SimpleMark Config", width=50)
    timezoneLabel = tk.Label(master=configFrame, text="Timezone")
    notif1Label = tk.Label(master=configFrame, text="Notification Time for Priority 1 (seconds)")
    notif2Label = tk.Label(master=configFrame, text="Notification Time for Priority 2 (seconds)")
    notif3Label = tk.Label(master=configFrame, text="Notification Time for Priority 3 (seconds)")
    notif4Label = tk.Label(master=configFrame, text="Notification Time for Priority 4 (seconds)")
    notif5Label = tk.Label(master=configFrame, text="Notification Time for Priority 5 (seconds)")
    remindLabel = tk.Label(master=configFrame, text="Time between reminder check (seconds)")

    #Entry creation
    timezoneEntry = tk.Entry(master=configFrame, width=20)
    notif1Entry = tk.Entry(master=configFrame, width=10)
    notif2Entry = tk.Entry(master=configFrame, width=10)
    notif3Entry = tk.Entry(master=configFrame, width=10)
    notif4Entry = tk.Entry(master=configFrame, width=10)
    notif5Entry = tk.Entry(master=configFrame, width=10)

    #remind time options
    options = [1,5,10]
    dropType = IntVar()
    prevRemindChoice = configData[7]
    if prevRemindChoice == options[0]:
        dropType.set(options[0])
    elif prevRemindChoice == options[1]:
        dropType.set(options[1])
    else:
        dropType.set(options[2])

    remindOption = OptionMenu(configFrame, dropType, *options)

    #Buttons
    saveConfigButton = tk.Button(
        master=configFrame,
        text="Save Config",
        width=20,
        height=1,
        bg="black",
        fg='white',
        command=lambda: saveConfigData(configData, configFrame, window, dropType.get())
    )

    backHomeButton = tk.Button(
        master=configFrame,
        text="Back",
        width=20,
        height=1,
        bg="black",
        fg='white',
        command=lambda: deleteFrame(configFrame, [True, window])
    )
    #inserting information
    timezoneEntry.insert(0, configData[0])
    notif1Entry.insert(0, configData[2])
    notif2Entry.insert(0, configData[3])
    notif3Entry.insert(0, configData[4])
    notif4Entry.insert(0, configData[5])
    notif5Entry.insert(0, configData[6])


    #item packing
    configLabel.pack()
    timezoneLabel.pack()
    timezoneEntry.pack()
    notif1Label.pack()
    notif1Entry.pack()
    notif2Label.pack()
    notif2Entry.pack()
    notif3Label.pack()
    notif3Entry.pack()
    notif4Label.pack()
    notif4Entry.pack()
    notif5Label.pack()
    notif5Entry.pack()
    remindLabel.pack()
    remindOption.pack()
    saveConfigButton.pack()
    backHomeButton.pack()

    #making new config data


'''
Updates the List on the page
windowInfo: List object containing the window, file, and listFrame information
'''
def updateList(list, window):

    listFrame = tk.Frame()
    listFrame.pack()
    window.title("SimpleMark List: {}".format(list.getName()))
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

    listNameLabel = tk.Label(master=listFrame, text="List: {}".format(list.getName()))
    listNameLabel.pack()

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
        command=lambda: editMark(None, list, 0, listFrame, window)
    )

    removeItemButton = tk.Button(
        master=listFrame,
        text="Remove Item",
        width=20,
        height=1,
        bg="black",
        fg='white',
        command=lambda: removeItem(markEntry.get(), list, listFrame, window)
    )

    removeListButton = tk.Button(
        master=listFrame,
        text="Delete List",
        width=20,
        height=1,
        bg="black",
        fg='white',
        command=lambda: deleteList(list,listFrame, window)
    )
    editMarkButton = tk.Button(
        master=listFrame,
        text="Edit Mark Information",
        width=20,
        height=1,
        bg="black",
        fg='white',
        command=lambda: editMark(markEntry.get(), list, 1, listFrame, window)
    )
    backButton = tk.Button(
        master=listFrame,
        text="Back Home",
        width=20,
        height=1,
        bg="black",
        fg='white',
        command=lambda: deleteFrame(listFrame, [True,window])
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
    backButton.pack()

    remindThread = threading.Thread(target=reminders, args=(list,))
    remindThread.start()

'''
Allows for changes to be made to specific marks
searchMarkName: String of the name of the mark to be edited
list: List object to be searched/added
option: Int value (0,1) of mark to be added/edited
'''
def editMark(searchMarkName, list, option, listFrame, window):

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
        command=lambda: addMark(mark, list, option, editMarkFrame, prioType, listFrame, window)
    )

    cancelMarkEditButton = tk.Button(
        master=editMarkFrame,
        text="Cancel",
        width=20,
        height=1,
        bg="black",
        fg='white',
        command=lambda: deleteFrame(editMarkFrame, [False])
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
        deleteFrame(editMarkFrame, [False])

'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
FUNCTIONS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
'''
Updates the list after a change was made
list: List object needed to be updated
frame: Tk frame editMarkClass
mainFrame: Tk Frame holding the create and open buttons
'''
def openListFromFile(window, file, mainFrame):

    if os.path.exists(file) and os.path.isfile(file):
        list = openList(file)
        if list is not None:
            print("Opened list from: {}".format(file))
            name = list.getName()
            window.title("SimpleMark: {}".format(name))
            if mainFrame != None:
                deleteFrame(mainFrame, [False])

            updateList(list, window)
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
def addMark(mark, list, option, frame, prioType, listFrame, window):
    #finding information from the frame
    objects = frame.winfo_children()
    name = objects[6].get()
    details = objects[7].get()
    deadline = objects[8].get()
    color = objects[9].get()
    prio = int(prioType.get())

    if isfloat(deadline):
        deleteFrame(frame, [False])
        deleteFrame(listFrame, [False])
        deadline = float(deadline)
        # creating new mark if adding, editing if edit
        if option == 0:
            mark = Mark(name, details, deadline, prio, color)
            doPass = list.add(mark)
            if doPass:
                saveList(list)
                updateList(list, window)
            else:
                updateList(list, window)
                tk.messagebox.showerror(title="SimpleMark", message="Name already used in list")
        else:

            mark.changeName(name)
            mark.changeDetails(details)
            mark.changeDeadline(deadline)
            mark.changePriority(prio)
            mark.changeColor(color)
            saveList(list)

            updateList(list, window)
    else:
        tk.messagebox.showerror(title="SimpleMark", message="Please enter a number for a deadline")
'''
removes item from list
markName: String name of mark to be removed
list: List object of mark to remove
listFrame: Tk Frame list frame
'''
def removeItem(markName, list, listFrame, window):
    mark = list.findMark(markName)
    if mark != None:
        #checks to see if last item in list
        if mark.getNext() == None and mark.getPrevious() == None:
            check = tk.messagebox.askyesno(title='SimpleMark',
                                           message="Deleting Mark '{}' will also delete the list. Continue?"
                                           .format(mark.getName()))
            if check:
                deleteList(list, listFrame, window)
        else:
            check = tk.messagebox.askokcancel(title="SimpleMark", message="This will remove mark '{}' from list '{}'. "
                                                                          "Are you sure?"
                                              .format(mark.getName(), list.getName()))
            # if user clicks ok, the item is removed from the list and the list is saved
            if check:
                list.remove(mark)
                saveList(list)
                deleteFrame(listFrame, [False])
                updateList(list, window)
    else:
        if markName == '':
            tk.messagebox.showerror(title="SimpleMark", message="Please enter the name of a mark in the list")
        else:
            tk.messagebox.showerror(title="SimpleMark", message="Mark {} not found in list {}".format(markName,
                                                                                                      list.getName()))

'''
Deletes list and file from computer
list: List object to be deleted
listFrame: Tk Frame listFrame
'''
def deleteList(list, listFrame, window):

    file = os.getcwd() + "\\ListData\\{}.txt".format(list.getName())

    check1 = tk.messagebox.askyesno(title="SimpleMark", message="Are you sure you want to remove list '{}'?"
                                    .format(list.getName()))
    if check1:
        check2 = tk.messagebox.askyesno(title="SimpleMark",message="Are you really sure?")
        if check2:
            print("Deleted list {} from {}".format(list.getName(), file))
            os.remove(file)
            deleteFrame(listFrame, [True, window])

'''
Saves the config data to file and updates it
configData: list that contains all configuration data
configFrame: Tk frame for config page
window: Tk object for the main window
remindTime: Time selected between reminders
'''
def saveConfigData(configData, configFrame, window, remindTime):
    #data starts at index 7
    options = configFrame.winfo_children()
    print(options)

    timezone = options[8].get()
    prio1 = options[9].get()
    prio2 = options[10].get()
    prio3 = options[11].get()
    prio4 = options[12].get()
    prio5 = options[13].get()

    #Makes sure all entered times entered are integers
    if isint(prio1) and isint(prio2) and isint(prio3) and isint(prio4) and isint(prio5):
        prio1 = int(prio1)
        prio2 = int(prio2)
        prio3 = int(prio3)
        prio4 = int(prio4)
        prio5 = int(prio5)
        remindTime = int(remindTime)

        configData[0] = timezone
        configData[2] = prio1
        configData[3] = prio2
        configData[4] = prio3
        configData[5] = prio4
        configData[6] = prio5
        configData[7] = remindTime

        saveConfig(configData)

        deleteFrame(configFrame, [True, window])
        print("Config Data saved")

    else:
        tk.messagebox.showerror(title="SimpleMark", message='All notif times must be numbers')

'''
Removes frame from screen
frame: Tk frame object to be deleted
openMain: list that checks if main needs to be opened
'''
def deleteFrame(frame, openMain):
    global notifRun
    notifRun = False
    frame.destroy()
    if openMain[0]:
        mainPage(openMain[1])

'''
Clears the frame that is sent to the function of objects
frame: tk frame to have objects removed
'''
def clearFrame(frame):
    for widget in frame.winfo_children():
        widget.destroy()
        print("object destroyed")
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

    if listName == '' or markName == '' or markDetails == '' or markDeadline == '' or markColor == '':
        tk.messagebox.showerror(title="SimpleMark", message="Please enter all information")
    else:
        if isfloat(markDeadline):
            markDeadline = float(markDeadline)
            #creates mark and list objects, and saves them to a new file
            mark = Mark(markName, markDetails, markDeadline, markPrio, markColor)
            list = List(listName, mark)
            file = saveList(list)

            openListFromFile(window, file, None)
            deleteFrame(frame, [False])
        else:
            tk.messagebox.showerror(title='SimpleMark', message="Please enter a number for deadline")
'''
gets the full path of the file
Returns: String value of the path of the file
choice: File being looked for
names: List containing all full names
paths: List containing all full paths
'''
def getPath(choice, names, paths):
    path = ''
    for i in range(len(names)):
        if choice == names[i]:
            path = paths[i]
    return path
'''
Checks if a value is float
num: value to be checked
'''
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
         return False

'''
Checks if number is integer
num: value to be checked
'''
def isint(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

'''
Runs reminders when list is open, cancels run when list is closed
list: List object of reminders to run
'''
def reminders(list):
    global notifRun
    notifRun = True
    checkTime = configData[7]
    timeZone = configData[0]
    notifTimes = [configData[2], configData[3], configData[4], configData[5], configData[6]]
    print(notifTimes)
    listLength = list.getLength()

    #Finding if notif has already been run for each variable
    mark = list.getHead()
    runAlready = []
    for i in range(listLength):
        prio = mark.getPrio()
        print(prio)
        if prio == 1:
            runAlready.extend([True, True, True, True, False])
        elif prio == 2:
            runAlready.extend([True, True, True, False, False])
        elif prio == 3:
            runAlready.extend([True, True, False, False, False])
        elif prio == 4:
            runAlready.extend([True, False, False, True, False])
        else:
            runAlready.extend([False, False, False, False, False])
        mark = mark.getNext()
    print(runAlready)
    #runs while the list is open
    while notifRun:
        print('checking notifs')
        runNotif(list, list.getLength(), timeZone, notifTimes, runAlready)
        time.sleep(checkTime)
    return
'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
MAIN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
configData = openConfig()
print(configData)
list = ""
if configData != None:
    # creates window and residual parts of the window itself
    window = tk.Tk()
    window.title("SimpleMark")
    mainPage(window)

    window.mainloop()
    global notifRun
    notifRun = True


else:
    print("Failed to load SimpleMark. Configuration file not found.")
    tkinter.messagebox.showerror(title="SimpleMark", message=
                                       "Failed to load SimpleMark. Configuration file not found.")
