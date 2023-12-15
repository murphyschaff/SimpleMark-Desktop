import datetime
import tkinter as tk
import re
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
ASCII_CHARS = 256

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
    elif not isint(hr) or int(hr) > 12 or int(hr) < 1:
        tk.messagebox.showerror(title="SimpleMark", message="Please enter a valid hour value")
    elif not isint(min) or int(min) > 59 or int(min) < 0:
        tk.messagebox.showerror(title="SimpleMark", message="Please enter a valid minute value")
    else:
        year = int(year)
        hr = int(hr)
        min = int(min)
        makeTime = True
        # Checking to see if months and dates match up
        #adds to the hour if PM is selected
        if hrType == "PM":
            hr = hr + 12
        #Makes through all checks, makes a datetime object
        if makeTime and isdate(year, month, day, hr, min):
            time = datetime.datetime(year, month, day, hr, min)
        else:
            tk.messagebox.showerror('SimpleMark', 'Date is invalid. Try again')

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
Checks if input is valid datetime object
'''
def isdate(year, month, day, hr, min):
    try:
        datetime.datetime(year, month, day, hr, min)
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

key: Key used to encode line (list of ascii values)
message: Message to encode
'''
def encode(key, message):
    output = ''
    # runs for length of input string
    for i in range(len(message)):
        #gets ascii value for each character, and gets key value
        letter = ord(message[i])
        keyLet = key[i]
        #adds letter to key value, and makes sure it will still be in the ascii range
        newChar = (letter + keyLet) % ASCII_CHARS
        output += '\\' + hex(newChar)
    #returns encoded string
    return output

'''
Decodes one-time-pad vignere ciphers
Returns: String of decoded information

key: key used to decrypt message 
ciphertext: ciphertext to dcode
'''
def decrypt(key, ciphertext):
    output = ''
    #runs for each letter of the ciphertext
    i = 1
    keyIndex = 0
    while i < len(ciphertext):
        val = ''
        while i < len(ciphertext) and ciphertext[i] != '\\':
            val += ciphertext[i]
            i += 1
        intVal = int(val, 16)

        output += chr((intVal - key[keyIndex]) % ASCII_CHARS)
        i += 1
        keyIndex += 1
    return output

'''
Generates the key for the vignere cipher
Returns: List representing the key

length: Int value of the length of the key
'''
def keyGen(length):
    key = []
    number = random.randint(32, 51)
    key.append(number)
    for _ in range(length - 1):
        number = random.randint(32, 255)
        key.append(number)
    return key

'''
Turns the alphabetical key into numbers
Returns: List of numbers representing the key

stringKey: String value of the key
'''
def stringToNumKey(stringKey):
    key = []
    i = 1
    while i < len(stringKey):
        val = ''
        while i < len(stringKey) and stringKey[i] != '\\':
            val += stringKey[i]
            i += 1
        intOutput = int(val, 16)
        key.append(intOutput)
        i += 1
    return key


'''
Turns the numerical key into a string of alphabetical letters
Returns: String representing the key

key: List of numbers representing the key
'''
def numToStringKey(key):
    output = ''
    for i in range(len(key)):
        num = key[i]
        output += '\\' + hex(num)
    return output


'''
Makes a random string of characters based on a length
Returns: String of random characters

length: Int value of length of string
'''
def randomstring(length):
    output = ''
    for _ in range(length):
        num = random.randint(32,255)
        output += '\\' + hex(num)
    return output

'''
Finds and returns an encoded string value based on the length of the string
Returns: encoded String value

line: full length string to be parsed
length: length of wanted string
'''
def findString(line, length):
    times = 0
    i = 1
    output = ''
    while times < length and i < len(line):
        val = ''
        while i < len(line) and line[i] != '\\':
            val += line[i]
            i += 1
        output += '\\' + val
        times += 1
        i += 1
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
                check.readline()
                listName = check.readline()
                listName = listName.strip()
                print('{} {}'.format(listName, name))
                if listName == name:
                    exists = True
            check.close()
    return exists

'''
Gets the length of the encoded message
key: string representing the key
message: string representing the message

Returns: [length, newkey, newmessage]
'''
def getEncodedLength(key, message):
    #getting first 3 characters of the key, adds into array for use in decrypt
    i = 1
    times = 0
    newKey = []
    while times < 3:
        val = ''
        while key[i] != '\\':
            val += key[i]
            i += 1
        newKey.append(int(val,16))
        i += 1
        times += 1
    key = key[i - 1:]

    #getting first 3 characters of the message, still made in encoded way
    i = 1
    times = 0
    newMessage = ''
    while times < 3:
        val = ''
        while message[i] != '\\':
            val += message[i]
            i += 1
        newMessage += '\\' + val
        i += 1
        times += 1
    message = message[i-1:]

    length = hextoint(decrypt(newKey, newMessage))

    return length, key, message
