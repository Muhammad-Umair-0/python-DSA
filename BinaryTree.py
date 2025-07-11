class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preOrderTraversal(node):
    if node is None:
        return 
    print(node.data, end=", ")
    preOrderTraversal(node.left)
    preOrderTraversal(node.right)

def postOrderTraversal(node):
    if node is None:
        return 
    postOrderTraversal(node.left)
    postOrderTraversal(node.right)
    print(node.data, end=", ")




root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD= TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG= TreeNode('G')
nodeH= TreeNode('H')
nodeI = TreeNode('I')


root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right= nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeC.right = nodeG
nodeC.left = nodeH

nodeD.right = nodeI

# it will print the F 
print(root.right.right.data)
# preorder traversal 
print("\n PreOrder Traversal")
preOrderTraversal(root)

print("\n PostOrder Traversal")
postOrderTraversal(root)






