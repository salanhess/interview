#coding=utf-8

class Node():
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

def preOrder(tree):
    if not tree:
        return
    print(tree.data)
    preOrder(tree.left)
    preOrder(tree.right)

def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print(root.data)
    inOrder(root.right)


tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))
print("====preorder====")
preOrder(tree)
print("====inOrder====")
inOrder(tree)