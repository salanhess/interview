#coding = utf-8
# refer to http://blog.csdn.net/bone_ace/article/details/46718683

class Node(object):
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

#15 层次遍历
def lookup(root):
    stack = [root]
    while stack:
        currrent = stack.pop(0)
        if currrent:
            print(currrent.data)
            if currrent.left:
                stack.append(currrent.left)
            if currrent.left:
                stack.append(currrent.right)

#15 深度遍历
def deep(root):
    if not root:
        return
    print(root.data)
    deep(root.left)
    deep(root.right)

#16 前序遍历 DLR
def preorder(root):
    if root:
        return
    print(root.data)
    deep(root.left)
    deep(root.right)

#17 中序遍历 LDR
def inorder(root):
    if root:
        return
    deep(root.left)
    print(root.data)
    deep(root.right)


tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))

'''
     1
    /  \
    3   2
   / \ / \
  7  6 5   4
 /
0
 '''
if __name__ == '__main__':
    lookup(tree)
    print("===========")
    deep(tree)
    print("===========")
    preorder(tree)
    print("===========")
    inorder(tree)
