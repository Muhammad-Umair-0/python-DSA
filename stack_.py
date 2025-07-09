stack = []

#push
stack.append("A")
stack.append("B")
stack.append("D")
print(f"stack {stack}")


#peek 
topElement = stack[-1]
print("Peek: ", topElement)

# pop 

pop_ele = stack.pop()
print(f"the poped elementis : {pop_ele}")

# stack after pop 
print(f"stack After pop {stack}")

#is Empty

isEmpty  = not bool(stack)
print("isEmpty: ", isEmpty)


#Size 
print("Size: ", len(stack))

# Creating stack using class

class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,element):
        return self.stack.append(element)
    
    def pop(self):
        if self.isEmpty():
            return "the Stack is Empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "the stack is Empty"
        return self.stack[-1]
    def isEmpty(self):
        return len(self.stack)==0
    
    def size(self):
        return len(self.stack)
    


# create a stack ot stack object
print("\n Calling the Class Object")
mystack = Stack() 
mystack.push('A')
mystack.push('B')
mystack.push('D')
mystack.push(7)


print("Stack", mystack.stack)
print(f"Pop  {mystack.pop()}")
print(f"Stack after the pop   {mystack.stack}")
print(f"Peek value of stack:   {mystack.peek()}")
print(f"MY Stck isEmpty  {mystack.isEmpty()}")
print(f"Size {mystack.size()}")




# Stack implementation using Linked List 

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size +=1
    
    def pop(self):
        if self.isEmpty():
            return "stack is Empty"
        popped_node = self.head
        self.head = self.head.next
        self.size  -=1
        return popped_node.value
    
    def peek(self):
        if self.isEmpty():
            return "stack is Empty"
        return self.head.value
    
    def isEmpty(self):
        return self.size ==0
    
    def stackSize(self):
        return self.size
    



# create a stack ot stack object
print("\n Calling the Class Object")
myStack = Stack()
myStack.push('A')
myStack.push('B')
myStack.push('D')
myStack.push(7)
# print("Stack", myStack)
print(f"Pop  {myStack.pop()}")
print(f"Stack after the pop   {myStack.pop}")
print(f"Peek value of stack:   {myStack.peek()}")
print(f"MY Stck isEmpty  {myStack.isEmpty()}")
print(f"Size {myStack.stackSize()}")
