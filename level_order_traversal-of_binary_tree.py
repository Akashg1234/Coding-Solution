class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

def solve(root,h):
    if root is None:
        return h
    else:
        return max(solve(root.left,h+1),solve(root.right,h+1))
def height(root):
    h=-1
    return solve(root,h)

def printGivenOrder(root,level):
    if root is None:
        return
    if level == 0:
        print(root.info, end=" ")
    elif level>0:
        printGivenOrder(root.left , level-1) 
        printGivenOrder(root.right , level-1)

def levelOrder(root):
    #Write your code here
    h =height(root)
    for i in range(0,h+1):
        printGivenOrder(root,i)



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)
