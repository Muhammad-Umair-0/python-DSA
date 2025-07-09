#  Single Linked List
 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None  # Fix: assign None, not 'next'


node1 = Node(2)
node2 = Node(5)
node3 = Node(6)
node4 = Node(8)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

currentNode = node1
print("The result for Single linked list is ")

while currentNode:
    print(currentNode.data, end="-->")
    currentNode = currentNode.next

print("null")


#double Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

node1 = Node(2)
node2 = Node(5)
node3 = Node(6)
node4 = Node(8)
node5 = Node(9)

node1.next = node2

node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.prev = node3
node4.next = node5

node5.prev = node4

print("\n Transversing forward ")
currentNode = node1
while currentNode:
    print(currentNode.data, end=" --> ")
    currentNode = currentNode.next
print("Null")

print("\n Transversing backward")

currentNode = node5
while currentNode:
    print(currentNode.data, end=" --> ")
    currentNode = currentNode.prev
print("Null")

#single Circular List
print("\n single circular list")

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None



node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1

currentNode = node1
startNode = node1

print(currentNode.data, end ="-->")
currentNode = currentNode.next

while currentNode != startNode:
    print(currentNode.data, end="-->")
    currentNode = currentNode.next
print("....")  


print("\n Double Circle")

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
        self.prev = None
        
node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2
node1.prev = node4

node2.prev = node1
node2.next = node3

node3.prev = node2
node3.next = node4

node4.prev = node3
node4.next = node1

print("\nTraversing forward:")
currentNode = node1
startNode = node1
print(currentNode.data, end=" -> ")
currentNode = currentNode.next

while currentNode != startNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
print("...")

print("\nTraversing backward:")
currentNode = node4
startNode = node4
print(currentNode.data, end=" -> ")
currentNode = currentNode.prev

while currentNode != startNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.prev
print("...")

# Linked List Operations 
print("Linked List Operations")



class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def traversePrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end ="-->")
        currentNode = currentNode.next
    print("null")


node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("\n Traversed Linked List ")
traversePrint(node1)


#  List to find the lowest number 


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def findLowest(head):
    minVal = head.data
    currentNode = head.next
    while currentNode:
        if currentNode.data < minVal:
            minVal = currentNode.data

        currentNode = currentNode.next
    return minVal

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(12)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
print("The Lowest number is ")
print(findLowest(node1))


# dlete a node in linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
    
def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end="-->")
        currentNode  = currentNode.next
    print("Null")

def delSpecificNode(head, nodeToDelete):

    if head == nodeToDelete:
        return head.next
    
    currentNode = head
    while currentNode.next and currentNode.next != nodeToDelete :
        currentNode = currentNode.next


    if currentNode.next is None:
        return head
    
    currentNode.next = currentNode.next.next

    return head



node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


print("Before Deletion : ")
traverseAndPrint(node1)



# deletion of nod
node1 = delSpecificNode(node1,node4)
print("\n after deletion ")
traverseAndPrint(node1)


# inseriton of Node

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
    
def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end="-->")
        currentNode  = currentNode.next
    print("Null")


def insertNodeatPosition(head, newNode, position):
    if position ==1:
        newNode.next = head
        return newNode
    
    currentNode = head
    for _ in range(position-2):
        if currentNode is None:
            break
        currentNode = currentNode.next

    newNode.next = currentNode.next
    currentNode.next = newNode
    return head



node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


print(" Origional list: ")
traverseAndPrint(node1)



# deletion of nod
newNode = Node(97)
node1 = insertNodeatPosition(node1,newNode,4)
print("\n after insertion ")
traverseAndPrint(node1)