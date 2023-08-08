from listmarkclass import *
from files import *
import time
from windowstoast import Toast
from notifications import *

mark1 = Mark("Mark1", "test", time.time(), 1, "blue")
time.sleep(1)
mark2 = Mark("Mark2", "test", time.time(), 2, "blue")
time.sleep(1)
mark3 = Mark("Mark3", "test", time.time(), 3, "blue")
time.sleep(1)
mark4 = Mark("Mark4", "test", time.time(), 4, "blue")
time.sleep(1)
mark5 = Mark("Mark5", "test", time.time(), 5, "blue")
time.sleep(1)

list = List("bob", mark1)
list.add(mark2)

list.add(mark3)
#print(mark3.getPrevious().getName())

list.add(mark4)

list.add(mark5)
list.list()

'''
list = openList('C:\\Users\\bluej\\OneDrive\\Documents\\SimpleMark\\SimpleMarkv1\\ListData\\bob.txt')
list.list()
print(list.getHead().getDeadline())
'''
'''
list.remove(mark5)
list.remove(mark1)
list.remove(mark2)
list.remove(mark3)
list.remove(mark4)
list.remove(mark5)
list.list()
print("ran")
'''


#print(list.getHead().getName())
saveList(list.getHead(), list.getName(), list.getLength())
path = 'C:\\Users\\bluej\\OneDrive\\Documents\\SimpleMark\\SimpleMarkv1\\ListData\\bob.txt'
newList = openList(path)
newList.list()

configData = ['US/Mountain', path, 900, 1800, 3600, 5400, 7200]
saveConfig(configData)
configData = openConfig()
print(configData)

notifTimes = [configData[2], configData[3], configData[4], configData[5], configData[6]]
runNotif(list, list.getLength(), configData[0], notifTimes)




'''
notif = Toast("SimpleMark", "Mark", ActivationType="protocol", Duration="long")
cwd = os.getcwd()
logo = cwd + "/logo.png"
notif.add_image("logo", placement="logo", hint_crop='circle')
notif.add_text("Test")
notif.show()
'''
'''
mark1 = Mark("Mark1", "test", 12, 3, "blue")
mark2 = Mark("Mark2", "test", 13, 3, "blue")
mark3 = Mark("Mark3", "test", 14, 3, "blue")
mark4 = Mark("Mark4", "test", 15, 3, "blue")
mark5 = Mark("Mark5", "test", 16, 3, "blue")
notif.show()print("reach1")


list = List("bob", mark1)

#list.list()


list.add(mark2)
list.add(mark3)
list.add(mark4)
list.add(mark5)
list.list()

print(list.getLength())


print("removing")
#list.remove(mark5)

list.remove(mark1)

list.remove(mark2)

list.remove(mark3)

list.remove(mark4)

list.remove(mark5)
list.list()
print(list.getLength())
'''

