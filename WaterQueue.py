class WaterQueue:
    # The node class is set up
    class Node:
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
    front = None
    rear = None


    # Constructor
    def _init_(self):
        self.front = None
        self.rear = None


    # Counts the number of nodes in the queue
    def count(self):
        count = 0
        n = self.front

        while n is not None:
            count = count + 1
            n = n.next

        return count


    # Returns a boolean value for whether or not the
    # queue is empty
    def isEmpty(self):
        if self.front == None:
            return True
        else:
            return False


    # Enters a new value to the queue
    def enqueue(self, value):
        if self.isEmpty():
            self.front = value
            self.rear = self.front
        else:
            self.rear.next = value
            self.rear = self.rear.next


    # Removes and returns the front value in the queue
    def dequeue(self):
        if self.isEmpty():
            print("Queue Empty")
        else:
            retValue = self.front
            self.front = self.front.next
            retValue.next = None
            return retValue.value

    # Returns the front value in the queue
    def peek(self):
        if self.isEmpty():
            print("Queue Empty")
        else:
            return self.front.value
