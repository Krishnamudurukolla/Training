class node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
class Bst:
    def __init__(self):
        self.root = None
    def create(self, val):
        if not self.root:
            self.root = node(val)
            return
        temp = self.root
        while temp:
            previous = temp
            if temp.val > val:
                temp = temp.left
            elif temp.val < val:
                temp = temp.right
            else:
                return 'Data already Exist'
        if previous.val > val:
            previous.left = node(val)
        else:
            previous.right = node(val)
    def inorder(self):
        if not self.root:
            return 'Tree Empty'
        def Traverse(node):
            if node:
                Traverse(node.left)
                print(node.val, end = ' ')
                Traverse(node.right)
        Traverse(self.root)
        print()
    def preorder(self):
        if not self.root:
            return 'Tree Empty'
        def Traverse(node):
            if node:
                print(node.val, end = ' ')
                Traverse(node.left)
                Traverse(node.right)
        Traverse(self.root)
        print()
    def postorder(self):
        if not self.root:
            return 'Tree Empty'
        def Traverse(node):
            if node:
                Traverse(node.left)
                Traverse(node.right)
                print(node.val, end = ' ')
        Traverse(self.root)
        print()
    def height(self, Node, Height = 0):
        if not Node:
            return Height - 1
        #print(Node.val, Height)
        return max(self.height( Node.left, Height + 1), self.height(Node.right, Height + 1))
    def summ(self, Node):
        if not Node:
            return 0
        return Node.val + self.summ(Node.left) + self.summ(Node.right)
    def Evensum(self, Node):
        if not Node:
            return 0
        return  (Node.val if not Node.val & 1 else 0) + self.Evensum(Node.left) + self.Evensum(Node.right)
    def Oddsum(self, Node):
        if not Node:
            return 0
        return  (Node.val if Node.val & 1 else 0) + self.Oddsum(Node.left) + self.Oddsum(Node.right)
    def diff(self):
        def absdiff(Node = self.root):
            if not Node:
                return 0
            return  (Node.val if Node.val & 1 else -Node.val) + absdiff(Node.left) + absdiff(Node.right)
        return abs(absdiff())
t = Bst()
t.create(3)
t.create(2)
t.create(1)
t.create(5)
t.create(4)
t.create(6)
print('Inorder:',end = ' ')
t.inorder()
print('Preorder:',end = ' ')
t.preorder()
print('Postorder:',end = ' ')
t.postorder()
print('Heigth:',t.height(t.root))
print('Total Sum:',t.summ(t.root))
print('Even Sum:',t.Evensum(t.root))
print('Odd Sum:',t.Oddsum(t.root))
print('Difference Sum:',t.diff())