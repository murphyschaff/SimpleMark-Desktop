import datetime
import tkinter as tk
import re
import string
import random
import os
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
        tk.messagebox.showerror(title="SimpleMark", message="Please enter a valid year value")
    elif not isint(hr) and 0 < hr < 13:
        tk.messagebox.showerror(title="SimpleMark", message="Please enter a valid hour value")
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

'''
Encodes a line of a file at once using a one-time-pad vignere cipher
Returns: String object of the encoded line

key: Key used to encode line
message: Message to encode
'''
def encode(key, message):
    numbers = []
    numbers.extend(range(0, 65))
    letters = list(string.ascii_letters)
    letters.append(' ')
    for i in range(9):
        letters.append(str(i))
    letters.append('-')
    letters.append(':')
    letters.append('.')

    keyLength = len(key)
    output = ''
    # runs for length of input string
    for i in range(len(message)):
        letter = message[i]
        findLetter = True
        x = 0
        # finds letter
        while findLetter:
            if letter == letters[x]:
                # gets corresponding number to letter
                number = numbers[x]
                # gets corresponding key to position in computer
                specKey = key[i % keyLength]
                # finds the new number based on key
                newNumber = (number + specKey) % 65
                # adds corresponding letter to output
                output = output + letters[newNumber]
                findLetter = False
            else:
                x = x + 1
    return output

'''
Decodes one-time-pad vignere ciphers
Returns: String of decoded information

key: key used to decrypt message
ciphertext: ciphertext to dcode
'''
def decrypt(key, ciphertext):
    numbers = []
    numbers.extend(range(0, 65))
    letters = list(string.ascii_letters)
    letters.append(' ')
    for i in range(9):
        letters.append(str(i))
    letters.append('-')
    letters.append(':')
    letters.append('.')

    output = ''
    #runs for each letter of the ciphertext
    for i in range(len(ciphertext)):
        letter = ciphertext[i]
        findLetter = True
        x = 0
        #finds the corresponding number to the ciphertext letter
        while findLetter:
            if letter == letters[x]:
                number = numbers[x]
                specKey = key[i]
                #does the opposite interaction as the encode
                newNumber = (number - specKey) % 65

                output = output + letters[newNumber]

                findLetter = False
            else:
                x = x + 1

    return output

'''
Generates the key for the vignere cipher
Returns: List representing the key

length: Int value of the length of the key
'''
def keyGen(length):
    key = []
    for i in range(length):
        number = random.randint(0, 64)
        if i == 0 and number == 52:
            number = number + 1
        key.append(number)
    return key

'''
Turns the alphabetical key into numbers
Returns: List of numbers representing the key

stringKey: String value of the key
'''
def stringToNumKey(stringKey):
    numbers = []
    numbers.extend(range(0,65))
    letters = list(string.ascii_letters)
    letters.append(' ')
    for i in range(9):
        letters.append(str(i))
    letters.append('-')
    letters.append(':')
    letters.append('.')

    key = []
    for i in range(len(stringKey)):
        letter = stringKey[i]
        findLetter = True
        x = 0
        while findLetter:
            if letter == letters[x]:
                number = numbers[x]
                key.append(number)
                findLetter = False
            else:
                x = x + 1
    return key


'''
Turns the numerical key into a string of alphabetical letters
Returns: String representing the key

key: List of numbers representing the key
'''
def numToStringKey(key):
    letters = list(string.ascii_letters)
    letters.append(' ')
    for i in range(9):
        letters.append(str(i))
    letters.append('-')
    letters.append(':')
    letters.append('.')
    output = ''
    for i in range(len(key)):
        num = key[i]
        output = output + letters[num]
    return output


'''
Makes a random string of characters based on a length
Returns: String of random characters

length: Int value of length of string
'''
def randomstring(length):
    letters = list(string.ascii_letters)
    letters.append(' ')
    for i in range(9):
        letters.append(str(i))
    letters.append('-')
    letters.append(':')
    letters.append('.')

    output = ''
    for i in range(length):
        number = random.randint(0,64)
        output = output + letters[number]
    return output

'''
Finds and returns an encoded string value based on the length of the string
Returns: encoded String value

line: full length string to be parsed
length: length of wanted string
'''
def findString(line, length):
    newString = ''
    #Removes the length part of the string from the string
    for i in range(3, len(line)):
        newString = newString + line[i]
    output = ''
    #finds the wanted part of the string from the remaining string
    for i in range(0, length):
        output = output + newString[i]
    return output

'''
Converts an integer value to a 3 bix hex string
Returns: String value representing hex

value: Integer value to be converted
'''
def inttohex(value):
    remainders = []
    holdDiv = int(value / 16)
    remainders.append(value % 16)
    value = holdDiv

    if value == 0:
        remainders.append(0)
        remainders.append(0)
    else:
        holdDiv = int(value / 16)
        remainders.append(value % 16)
        value = holdDiv
        if value == 0:
            remainders.append(0)
        else:
            remainders.append(value % 16)


    output = ''
    hex = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    for i in range(len(remainders)):
        output = output + hex[remainders[(len(remainders) - 1) - i]]
    type(output)
    return output

'''
Converts 3 char string hex value into an integer object
Returns: Integer value representation

string: String value of 3 chars
'''
def hextoint(string):
    hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    output = 0
    for i in range(len(string)):
        char = string[i]
        findValue = True
        x = 0
        while findValue:
            if char == hex[x]:
                findValue = False
                output = output + (x * (16 ** (len(string) - (i+1))))
                #print('{} {}'.format(x,(16 ** (len(string) - (i+1)))))
            else:
                x = x + 1
    return output

'''
Checks for existence of file already
Returns: True if list exists, False if not

name: Name of thing to be checked for
'''
def checkFile(name):
    cwd = os.getcwd()
    dir = cwd + "\\ListData"
    files = os.listdir(dir)
    names = []
    paths = []
    exists = False

    for i in range(len(files)):
        path = dir + "\\" + files[i]
        if os.path.exists(path) and os.path.isfile(path):
            check = open(path, 'r')
            watermark = check.readline()
            watermark = watermark.strip()
            if watermark == "SimpleMarkListType":
                listName = check.readline()
                listName = listName.strip()
                if listName == name:
                    exists = True
    return exists