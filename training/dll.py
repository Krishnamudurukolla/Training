class node:
    def __init__(self,u):
        self.data = u
        self.next = None
        self.prev = None
class dll:
    def __init__(self):
        self.head = None
        self.tail = None
    def addBack(self,x):
        if self.head==None:
            self.head=node(x)
            self.tail=self.head
        else:
#             self.tail.next=node(x)
#             self.tail.next.prev=self.tail
            temp = node(x)
            self.tail.next = temp
            temp.prev = self.tail
            self.tail = self.tail.next
    def addFront(self,x):
        if self.head==None:
            self.head=node(x)
            self.tail=self.head
        else:
            temp = node(x)
            temp.next = self.head
            self.head.prev = temp
            self.head = temp
    def deleteFront(self):
        if self.head==None:
            print(None)
        else:
            self.head=self.head.next
            self.head.prev=None
    def deleteBack(self):
        if self.tail==None:
            print(None)
        else:
            self.tail = self.tail.prev
            self.tail.next = None
    def linearSearch(self,x):
        if self.head==None:
            print(None)
        else:
            temp = self.head
            temp1= self.tail
            while temp!=None and temp1!=None:
                if temp.data==x:
                    return "Found"
                if temp1.data==x:
                    return "Found"
                temp=temp.next
                temp1=temp1.prev
            return "NotFound"
    def traverseFront(self):
        if self.head==None:
            print(None)
        else:
            temp=self.head
            while temp!=None:
                print(temp.data)
                temp=temp.next
    
    def traverseReverse(self):
        if self.head==None:
            print(None)
        else:
            temp=self.tail
            while temp!=None:
                print(temp.data)
                temp=temp.prev
            
a = dll()
a.addFront(10)
a.addBack(20)
a.addBack(30)
a.addBack(40)
a.addFront(5)
a.deleteFront()
a.deleteBack()
a.traverseFront()
#a.traverseReverse()
print(a.linearSearch(40))