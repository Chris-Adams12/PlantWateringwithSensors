########################################################################
# Chris Adams
# 04/01/22
# This file holds the linked list class to hold the plants
########################################################################

class LinkedList:
    # The Node class is established
    class Node:
        # value = None
        # next = None

        def __init__(self, *args):

            if len(args) == 2:
                self.value = args[0]
                self.next = args[1]

            elif len(args) == 1:
                self.value = args[0]
                self.next = None

            else:
                print("Invalid number of parameters")


    # The variables are declared
    first = None
    last = None

    # Constructor
    def _init_(self):
        self.first = None
        self.last = None


    # Counts the number of nodes in the linked list
    def count(self):
        count = 0
        n = self.first

        while n is not None:
            count = count + 1
            n = n.next

        return count


    # Returns a boolean value for whether or not the
    # linked list is empty
    def isEmpty(self):
        if self.first == None:
            return True
        else:
            return False


    # Adds a node of a given value to the linked list
    def add(self, value):
        if self.isEmpty():
            self.first = self.Node(value)
            self.last = self.first
        else:
            self.last.next = self.Node(value)
            self.last = self.last.next


    # Removes a node of a specific value from the list
    def remove(self, val):
        if self.isEmpty():
            print("No Plants Entered")
        else:
            pred = self.first

            for i in range(self.count()):
                if pred.value.name == val:
                    pred.value = pred.next.value
                    pred.next = pred.next.next
                    break
                else:
                    pred = pred.next
            else:
                print('No plant found with the name ', val)
                
    
    # This method finds the node with a given index
    def findIndex(self, index):
        i = self.first
        counter = 0
        while i is not None and index < self.count():
            if counter == index:
                return i
            else:
                i = i.next
                counter = counter + 1
                
    # This method finds the node with a given plant name
    def findName(self, name):
        i = self.first
        
        while i is not None:
            if i.value.name == name:
                return i
            else:
                i = i.next
                
        #if the value isn't found, return None
        return None
                

    # This method finds the node with a given sensorPin
    def findSensorPin(self, pin):
        i = self.first

        while i is not None:
            if i.value.sensorPin == pin:
                return i
            else:
                i = i.next

        #if the value isn't found, return None
        return None



    # This method displays all values of the nodes
    def list(self):
        e = self.first

        while e is not None:
            print(e.value.name, " ")
            e = e.next
            
    

