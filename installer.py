import tkinter as tk
import tkinter.messagebox
from tkinter import *
import datetime
import os
import shutil

'''
Window class for installer application
'''
class Installer(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("SimpleMark Installer")
        self.protocol("WM_DELETE_WINDOW", self.on_exit)
        self.page()

    def on_exit(self):
        if tk.messagebox.askyesno("SimpleMark Installer", "Are you sure you want to quit installation?"):
            self.destroy()

    '''
    Runs the main installer page
    '''
    def page(self):
        frame = tk.Frame()
        frame.pack()
        # object creation
        greeting = tk.Label(master=frame, text="SimpleMark Installer")
        description = tk.Label(
            master=frame,
            text='SimpleMark is a reminders program created by Murphy Schaff. \nPlease choose among the following'
                 ' options to install SimpleMark:'
        )
        # INSTALLATION LOCATION
        locationLabel = tk.Label(master=frame, text='Installation Location:')
        locationEntry = tk.Entry(master=frame, width=50)
        cwd = os.getcwd()
        locationEntry.insert(0, cwd)

        # CONFIG DEFAULTS
        defaultsLabel = tk.Label(master=frame, text="Config Default Values:")
        timezoneLabel = tk.Label(master=frame, text="Timezone")
        notif1Label = tk.Label(master=frame, text="Notification Time for Priority 1 (seconds)")
        notif2Label = tk.Label(master=frame, text="Notification Time for Priority 2 (seconds)")
        notif3Label = tk.Label(master=frame, text="Notification Time for Priority 3 (seconds)")
        notif4Label = tk.Label(master=frame, text="Notification Time for Priority 4 (seconds)")
        notif5Label = tk.Label(master=frame, text="Notification Time for Priority 5 (seconds)")
        remindLabel = tk.Label(master=frame, text="Time between reminder check (seconds)")
        timezoneEntry = tk.Entry(master=frame, width=30)
        notif1Entry = tk.Entry(master=frame, width=10)
        notif2Entry = tk.Entry(master=frame, width=10)
        notif3Entry = tk.Entry(master=frame, width=10)
        notif4Entry = tk.Entry(master=frame, width=10)
        notif5Entry = tk.Entry(master=frame, width=10)
        currentTimeZone = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
        timezoneEntry.insert(0, currentTimeZone)
        notif1Entry.insert(0, 900)
        notif2Entry.insert(0, 1800)
        notif3Entry.insert(0, 3600)
        notif4Entry.insert(0, 5400)
        notif5Entry.insert(0, 7200)
        # Reminders time
        remindOpt = [1, 5, 10]
        remindType = IntVar()
        remindType.set(remindOpt[0])
        remindMenu = OptionMenu(frame, remindType, *remindOpt)

        # BUTTON
        installButton = tk.Button(
            master=frame,
            text="Install SimpleMark",
            width=30,
            height=5,
            bg="black",
            fg='white',
            command=lambda: self.install(frame, remindType)
        )

        # Object packing
        greeting.pack()
        description.pack()
        locationLabel.pack()
        locationEntry.pack()
        defaultsLabel.pack()
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
        remindMenu.pack()
        installButton.pack()

    '''
    Installs the applicaiton
    
    frame: installer frame
    shortcutOption: options for the desktop shortcut
    remindType: options for the reminders type values
    '''

    def install(self, frame,remindType):
        remindVal = int(remindType.get())
        options = frame.winfo_children()
        installL = options[3].get()
        timezone = options[12].get()
        n1 = options[13].get()
        n2 = options[14].get()
        n3 = options[15].get()
        n4 = options[16].get()
        n5 = options[17].get()
        if installL == '' or timezone == '' or n1 == '' or n2 == '' or n3 == '' or n4 == '' or n5 == '':
            tk.messagebox.showerror('SimpleMark Installer', 'You must provide data for all types')
        else:
            if isint(n1) and isint(n2) and isint(n3) and isint(n4) and isint(n5):
                if os.path.exists(installL) and os.path.isdir(installL):
                    #checks and sees if the SimpleMark Desktop file already exists at location
                    dirCont = os.listdir(installL)
                    majorFiles = 0
                    for i in dirCont:
                        if i == 'SimpleMark Desktop':
                            majorFiles = 1
                    if majorFiles == 0:
                        if tk.messagebox.askyesno('SimpleMark Installer',
                                                  'Are you sure you want to install SimpleMark with '
                                                  'the following attributes:'
                                                  '\nInstaller Location: {}\n'
                                                  'Timezone: {}\n'
                                                  'Notification Time for Priority 1: {} s\n'
                                                  'Notification Time for Priority 2: {} s\n'
                                                  'Notification Time for Priority 3: {} s\n'
                                                  'Notification Time for Priority 4: {} s\n'
                                                  'Notification Time for Priority 5: {} s\n'
                                                  'Timezone and Priority values can be changed later'.format(
                                                      installL, timezone, n1, n2, n3, n4, n5)):
                            mainFile = installL + "\\SimpleMark Desktop"
                            os.mkdir(mainFile)
                            #Making Configuration File
                            configDir = mainFile + "\\config"
                            os.mkdir(configDir)
                            configFile = open(configDir + "\\config.txt", 'w')
                            configFile.write("TimeZone: {}\n".format(timezone))
                            configFile.write("Previous List: {}\n".format(''))
                            configFile.write("Notif for prio 1: {}\n".format(n1))
                            configFile.write("Notif for prio 2: {}\n".format(n2))
                            configFile.write("Notif for prio 3: {}\n".format(n3))
                            configFile.write("Notif for prio 4: {}\n".format(n4))
                            configFile.write("Notif for prio 5: {}\n".format(n5))
                            configFile.write("Time between reminder check: {}\n".format(remindVal))
                            configFile.close()

                            #create List Directory
                            os.mkdir(mainFile + '\\ListData')

                            #copying all proper files to main file
                            cwd = os.getcwd()
                            shutil.copy('SimpleMark.py', mainFile)
                            shutil.copy('notifications.py', mainFile)
                            shutil.copy('miscFunctions.py', mainFile)
                            shutil.copy('files.py', mainFile)
                            shutil.copy('listmarkclass.py', mainFile)
                            shutil.copy('SimpleMark Desktop.lnk', mainFile)

                            tk.messagebox.showinfo("SimpleMark Installer", 'SimpleMark has been installed at {}'
                                                   .format(mainFile))
                            self.destroy()
                    else:
                        tk.messagebox.showerror('SimpleMark Installer',
                                                'It seems as though SimpleMark already exists at this location.')
                else:
                    tk.messagebox.showerror('SimpleMark Installer', 'Please enter an valid directory')
            else:
                tk.messagebox.showerror('SimpleMark Installer', 'Please enter an integer value for notif times')


def isint(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


Installer().mainloop()
