import datetime
import tkinter as tk
import re
'''
Takes given data and converts into datetime.datetime object
Returns: Datetime.datetime object, None if invalid date

year: Int value of year
monthTxt: String value of month
day: Int value of day
hr: Int value of hour
min: Int value of min
hrType: String value (AM, PM)
configData: list of configuration data
'''
def createDatetime(year, monthTxt, day, hr, min, hrType, configData):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    month = 0
    time = None

    #finds corresponding month
    for i in range(len(months)):
        if months[i] == monthTxt:
            month = i + 1

    #Basic Value checking
    if not isint(year):
        tk.messagebox.showerror(title="SimpleMark", message="Please enter a valid year (integer value)")
    elif not isint(hr) and 0 < hr < 13:
        tk.messagebox.showerror(title="SimpleMark", message="Please enter a valid hour")
    elif not isint(min) and 0 < min < 60:
        tk.messagebox.showerror(title="SimpleMark", message="Please enter a valid minute value")
    else:
        year = int(year)
        hr = int(hr)
        min = int(min)
        makeTime = True
        # Checking to see if months and dates match up
        if month == 2:
            if day > 29:
                tk.messagebox.showerror(title="SimpleMark", message="{} does not have {} days. Try again"
                                        .format(monthTxt, day))
                makeTime = False
        elif month == 4 or month == 6 or month == 9 or month == 11:
            if day > 30:
                tk.messagebox.showerror(title="SimpleMark", message="{} does not have {} days. Try again"
                                        .format(monthTxt, day))
                makeTime = False
        #adds to the hour if PM is selected
        if hrType == "PM":
            hr = hr + 12
        #Makes through all checks, makes a datetime object
        if makeTime:
            time = datetime.datetime(year, month, day, hr, min)

    return time

'''
Attempts to read a string as a datetime object
Returns: Datetime object of the time represented in the string

string: String value to be turned into datetime object
'''
def translateDatetime(string):
    regex = re.compile(r'(\d\d\d\d)-(\d\d)-(\d\d) (\d\d):(\d\d):(\d\d)')
    groups = regex.findall(string)

    year = int(groups[0][0])
    month = int(groups[0][1])
    day = int(groups[0][2])
    hr = int(groups[0][3])
    min = int(groups[0][4])

    time = datetime.datetime(year, month, day, hr, min)
    return time

'''
Gets the entry data from the datetime object
Returns: List of each item in the datetime object [year, month, day, hr, min, hrType]

time: datetime object in question
'''
def datetimeToList(time):

    year = time.strftime('%Y')
    month = time.strftime('%m')
    month = int(month)
    day = time.strftime('%d')
    hr = time.strftime('%H')
    min = time.strftime('%M')
    min = int(min)
    hrType = 'AM'

    if min > 12:
        hrType = 'PM'

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
              "November", "December"]
    wordMonth = months[month - 1]

    return[year, wordMonth, day, hr, min, hrType]


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
