'''
Defines the List and Mark Classes, the strucutre of the linked lists
'''


class List:

    def __init__(self, name, head):
        self.name = name
        self.head = head 
        self.length = 1

    '''
    Adds a new mark to the list, based on deadline time
    newMark: Mark object to add to list
    '''
    def add(self, newMark):
        #checking for same name first
        print('hi')
        mark = self.head
        doPass = True
        while mark.getNext() != None:
            if newMark.getName() == mark.getName():
                #error, invalid name
                print("Error: Name already used")
                doPass = False
            mark = mark.getNext()
                
        if doPass == True:
            if self.length == 1:
                #one item in the list currently
                if self.head.getDeadline() >= newMark.getDeadline():
                    tmp = self.head
                    tmp.setPrevious(newMark)
                    self.head = newMark
                    self.head.setNext(tmp)
                else:
                    self.head.setNext(newMark)
            else:
                #more than one item in the list
                current = self.head
                run = True
                #checks the head value and replaces it if it is replaced
                if self.head.getDeadline() >= newMark.getDeadline():
                    tmp = self.head
                    tmp.setPrevious(newMark)
                    self.head = newMark
                    self.head.setNext(tmp)
                    run = False
                #If the head value is not the one replaced
                while run:
                    current = current.getNext()
                    #if new should go in front of current, closer deadline
                    if current.getDeadline() >= newMark.getDeadline():
                        previous = current.getPrevious()
                        
                        previous.setNext(newMark)
                        newMark.setPrevious(previous)
                        newMark.setNext(current)
                        current.setPrevious(newMark)
                        run = False
                    else:
                        # if last item in the list
                        if current.getNext() == None:
                            run = False
                            current.setNext(newMark)
                            newMark.setPrevious(current)
                        #otherwise iterate again.
            self.length = self.length + 1
            return doPass
        else:
            return doPass

    '''
    Removes mark with certain name from list
    toRemove: string name of mark to remove from list
    '''
    def remove(self, toRemove):
        self.length = self.length - 1

        if self.length > 0:
            mark = self.head
            #removing head of list
            if mark == toRemove:
                tmp = self.head
                self.head = self.head.getNext()
                del tmp
            else:
                #removing from middle of list
                while mark.getNext() != None:
                    mark = mark.getNext()
                    if mark == toRemove:
                        previous = mark.getPrevious()
                        next = mark.getNext()
                        previous.setNext(next)
                        if next != None:
                            next.setPrevious(previous)
        else:
            self.head = None

    '''
    Finds a mark in the list based off the name
    Returns: Mark object of the mark in question, None if not found
    name: String name of the mark to be found
    '''
    def findMark(self, name):
        mark = self.head
        markReturn = ''
        markFound = False
        doContinue = True
        while markFound is False and doContinue:
            if mark.getName() == name:
                markReturn = mark
                markFound = True
            if mark.getNext() == None:
                doContinue = False
            else:
                mark = mark.getNext()

        if markFound:
            return markReturn
        else:
            return None
            
                    
    '''
    Lists all marks within the list (testing purposes)
    '''
    def list(self):
        if self.length > 0:
            mark = self.head
            print(mark.getName())
            if mark.getNext() != None:
                mark = mark.getNext()
                while mark.getNext() != None:
                    #prints each item in the list
                    print(mark.getName())
                    mark = mark.getNext()
                print(mark.getName())
        else:
            return None
            
    #Returns length of list     
    def getLength(self):
        return self.length

    #Returns the Mark value to the head of the list
    def getHead(self):
        return self.head

    #Returns name of list
    def getName(self):
        return self.name




class Mark:
    #Each mark has a name, details, priority level, and color. All of which can be changed
    def __init__(self, name, details, deadline, priority, color):
        self.name = name
        self.details = details
        self.deadline = deadline
        self.priority = priority
        self.color = color

        self.next = None
        self.previous = None

    #Getters
    def getName(self):
        return self.name

    def getDetails(self):
        return self.details

    def getDeadline(self):
        return self.deadline

    def getPrio(self):
        return self.priority

    def getColor(self):
        return self.color

    def getNext(self):
        return self.next
    
    def getPrevious(self):
        return self.previous

    #Setters
    def changeName(self, newName):
        self.name = newName

    def changeDetails(self, newDetails):
        self.details = newDetails

    def changeDeadline(self, newDeadline):
        self.deadline = newDeadline

    def changePriority(self, newPrio):
        self.priority = newPrio

    def changeColor(self, newColor):
        self.color = newColor

    def setNext(self, next):
        self.next = next

    def setPrevious(self, previous):
        self.previous = previous