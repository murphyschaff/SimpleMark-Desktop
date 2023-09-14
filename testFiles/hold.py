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
    markYearLabel = tk.Label(master=createFrame, text="Year")
    markMonthLabel = tk.Label(master=createFrame, text="Month")
    markDayLabel = tk.Label(master=createFrame, text="Day")
    markHrLabel = tk.Label(master=createFrame, text="Hour")
    markMinLabel = tk.Label(master=createFrame, text="Minute")
    markPrioLabel = tk.Label(master=createFrame, text="Priority")
    markColorLabel = tk.Label(master=createFrame, text="color")

    # creation of text boxes
    listNameBox = tk.Entry(master=createFrame, width=30)
    descriptionBox = tk.Entry(master=createFrame, width=30)
    nameBox = tk.Entry(master=createFrame, width=30)
    yearBox = tk.Entry(master=createFrame, width=30)
    hourBox = tk.Entry(master=createFrame, width=30)
    minBox = tk.Entry(master=createFrame, width=30)
    colorBox = tk.Entry(master=createFrame, width=30)
    # prio option menu
    options = [1, 2, 3, 4, 5]
    prioType = IntVar()
    prioType.set(1)
    prioBox = OptionMenu(createFrame, prioType, *options)

    #Month, day, time type option menus
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
            30, 31]
    hrTypeO = ["AM", "PM"]

    monthType = StringVar()
    monthType.set(months[0])
    dayType = IntVar()
    dayType.set(days[0])
    hrType = StringVar()
    hrType.set(hrTypeO[0])

    monthMenu = OptionMenu(createFrame, monthType, *months)
    dayMenu = OptionMenu(createFrame, dayType, *days)
    hrMenu = OptionMenu(createFrame, hrType, *hrTypeO)

    #Button creation
    saveListButton = tk.Button(
        master=createFrame,
        text="Save List",
        width=20,
        height=1,
        bg="black",
        fg='white',
        command=lambda: saveAndOpenList(window, createFrame, prioType, monthType.get(), dayType.get(), hrType.get())
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
    markYearLabel.pack()
    yearBox.pack()
    markMonthLabel.pack()
    monthMenu.pack()
    markDayLabel.pack()
    dayMenu.pack()
    markHrLabel.pack()
    hourBox.pack()
    markMinLabel.pack()
    minBox.pack()
    hrMenu.pack()
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

    listNameLabel = tk.Label(master=listFrame, text="List: {}\n Mark Name: Details, Deadline, Priority".format(list.getName()))
    listNameLabel.pack()

    listLabel = tk.Label(
        master=listFrame,
        text=listString,
        width=50
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

    #Starts the notification threads to run in the background
    remindThread = threading.Thread(target=reminders, args=(list, window,))
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
    markYearLabel = tk.Label(master=editMarkFrame, text="Year")
    markMonthLabel = tk.Label(master=editMarkFrame, text="Month")
    markDayLabel = tk.Label(master=editMarkFrame, text="Day")
    markHrLabel = tk.Label(master=editMarkFrame, text="Hour")
    markMinLabel = tk.Label(master=editMarkFrame, text="Minute")
    prioLabel = tk.Label(master=editMarkFrame, text="Mark Priority")
    colorLabel = tk.Label(master=editMarkFrame, text="Mark Color")

    #creation of text boxes
    nameBox = tk.Entry(master=editMarkFrame, width=30)
    descriptionBox = tk.Entry(master=editMarkFrame, width=30)
    yearBox = tk.Entry(master=editMarkFrame, width=30)
    hrBox = tk.Entry(master=editMarkFrame, width=30)
    minBox = tk.Entry(master=editMarkFrame, width=30)
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

    #Month, day, and 12hr option menus
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
            30, 31]
    hrTypeO = ["AM", "PM"]

    monthType = StringVar()
    monthType.set(months[0])
    dayType = IntVar()
    dayType.set(days[0])
    hrType = StringVar()
    hrType.set(hrTypeO[0])

    monthMenu = OptionMenu(editMarkFrame, monthType, *months)
    dayMenu = OptionMenu(editMarkFrame, dayType, *days)
    hrMenu = OptionMenu(editMarkFrame, hrType, *hrTypeO)

    #adding details if the mark already exists
    if option ==1:

        deadlineList = datetimeToList(deadline)

        nameBox.insert(0, "{}".format(name))
        descriptionBox.insert(0, "{}".format(details))
        yearBox.insert(0, "{}".format(deadlineList[0]))
        hrBox.insert(0, "{}".format(deadlineList[3]))
        minBox.insert(0, "{}".format(deadlineList[4]))
        colorBox.insert(0, "{}".format(color))

        monthType.set(deadlineList[1])
        dayType.set(deadlineList[2])
        hrType.set(deadlineList[5])

    #button definitions
    saveMarkButton = tk.Button(
        master=editMarkFrame,
        text='{}'.format(buttonText),
        width=20,
        height=1,
        bg="black",
        fg='white',
        command=lambda: addMark(mark, list, option, editMarkFrame, prioType, monthType.get(), dayType.get(),
                                hrType.get(), listFrame, window)
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
        markYearLabel.pack()
        yearBox.pack()
        markMonthLabel.pack()
        monthMenu.pack()
        markDayLabel.pack()
        dayMenu.pack()
        markHrLabel.pack()
        hrBox.pack()
        markMinLabel.pack()
        minBox.pack()
        hrMenu.pack()
        prioLabel.pack()
        prioDrop.pack()
        colorLabel.pack()
        colorBox.pack()
        saveMarkButton.pack()
        cancelMarkEditButton.pack()
    else:
        deleteFrame(editMarkFrame, [False])
