#coding = utf-8
# refer to http://blog.csdn.net/bone_ace/article/details/46718683

class Node():
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right


#层次遍历
def lookup(root):
    stack = [root]
    while stack:
        currrent = stack.pop(0)
        if currrent:
            print(currrent.data)
            if currrent.left:
                stack.append(currrent.left)
            if currrent.right:
                stack.append(currrent.right)

#前序遍历/深度遍历 DLR
def preorder(root):
    if not root:
        return
    print(root.data)
    preorder(root.left)
    preorder(root.right)

#中序遍历 LDR
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)

#后序遍历 LRD
def backorder(root):
    if not root:
        return
    backorder(root.left)
    backorder(root.right)
    print(root.data)

'''
       1
     /   \
    3     2
   / \   / \
  7  6   5  4
 /
0
层次遍历： 1 3 2 7 6 5 4
先序遍历 DLR: 1 3 7 0 6 2 5 4
中序遍历 LDR: 0 7 3 6 1 5 2 4
后序遍历 LRD: 0 7 6 3 5 4 2 1
 '''
if __name__ == '__main__':
    tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))
    lookup(tree)
    print("====lookup end=======")
    preorder(tree)
    print("====preorder end=======")
    inorder(tree)
    print("====inorder end=======")
    backorder(tree)
    print("====backorder end=======")
