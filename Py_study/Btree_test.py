#coding=utf-8

class Node():
   def __init__(self,data,left=None,right=None):
       self.data =data
       self.left = left
       self.right = right

def preOrder(root):
    if not root:
        return
    print(root.data)
    preOrder(root.left)
    preOrder(root.right)

def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print(root.data)
    inOrder(root.right)

def LRD(root):
    if not root:
        return
    LRD(root.left)
    LRD(root.right)
    print(root.data)

#层次遍历
def lookup(root):
    stack = [root]
    while stack:
        current = stack.pop(0)
        print(current.data)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)


tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))
print("====preorder====")
preOrder(tree)
print("====inOrder====")
inOrder(tree)
print("====LRD====")
LRD(tree)
print("====lookup====")
lookup(tree)