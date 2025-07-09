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


