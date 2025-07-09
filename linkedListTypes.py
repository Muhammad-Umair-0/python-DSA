#  Single Linked List
 
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


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

