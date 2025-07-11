
# Queue 

queue = []

#Enqueue
queue.append('A')
queue.append('B')
queue.append('C')
print(queue)

# Dequeue
element = queue.pop(0)
print("The popo element is ", element)

# peek 
frontElement = queue[0]
print("peek : " , frontElement)

#isEmpty
isEmpty = not bool(queue)
print("is Empty :", isEmpty)

print("size: ", len(queue))


# explixity with class
class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self,element):
        self.queue.append(element)
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is EMpty"
        return self.queue.pop(0)
    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
    def isEmpty(self):
        return len(self.queue) ==0
        
    def size(self):
         return len(self.queue)


myQueue = Queue()
myQueue.enqueue('A')
myQueue.enqueue('C')
myQueue.enqueue('F')

print("Queue :", myQueue.queue)

print("DEqueue :", myQueue.dequeue())

print("Peek", myQueue.peek())

print("isEmpty :", myQueue.isEmpty())

print("size", myQueue.size())



#Queue with Linked List

class Node:
    def __init__(self, data):
        self.data =data 
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def enqueue(self,element):
        new_node = Node(element)
        if self.rear is None:
            self.front = self.rear = new_node
            self.length +=1
            return 
        
        self.rear.next = new_node
        self.rear = new_node
        self.length += 1

    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        temp = self.front
        self.front = temp.next
        self.length -=1
        if self.front is None:
            self.rear = None
        return temp.data
    
    def peek(self):
        if self.isEmpty():
            return " The Queue is Empty"
        return self.front.data
    
    def isEmpty(self):
        return self.length ==0
    
    def size(self):
        return self.length
    
    def printQueue(self):
        temp = self.front
        while temp:
            print(temp.data, end="")
            temp = temp.next
        print()


myQueue = Queue()
myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')
print("Queue: ", end=' ')
myQueue.printQueue()

print("Dequeue: ", myQueue.dequeue())

print("Peek: ", myQueue.peek())

print("isEmpty: ", myQueue.isEmpty())

print("Size:", myQueue.size())

