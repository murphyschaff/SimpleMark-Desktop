from listmarkclass import *

mark1 = Mark("Mark1", "test", 16, 1, "blue")
mark2 = Mark("Mark2", "test", 12, 2, "blue")
mark3 = Mark("Mark3", "test", 14, 3, "blue")
mark4 = Mark("Mark4", "test", 13, 4, "blue")
mark5 = Mark("Mark5", "test", 12, 5, "blue")

list = List(mark1)
list.add(mark2)

list.add(mark3)
#print(mark3.getPrevious().getName())

list.add(mark4)

list.add(mark5)
list.list()

list.remove(mark5)
list.remove(mark1)
list.remove(mark2)
list.remove(mark3)
list.remove(mark4)
list.remove(mark5)
list.list()
print("ran")

print("hello there")

'''
mark1 = Mark("Mark1", "test", 12, 3, "blue")
mark2 = Mark("Mark2", "test", 13, 3, "blue")
mark3 = Mark("Mark3", "test", 14, 3, "blue")
mark4 = Mark("Mark4", "test", 15, 3, "blue")
mark5 = Mark("Mark5", "test", 16, 3, "blue")


list = List(mark1)

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

