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