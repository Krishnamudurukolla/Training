class node:
    def __init__(self, val):
        self.val = val
        self.prev = self.next = None
class List:
    def __init__(self):
        self.head = self.next = None
        self.len = 0
    def append(self, val):
        if not self.head:
            self.head = self.tail = node(val)
        else:
            self.tail.next = node(val)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
        self.len += 1
    def add_at_front(self, val):
        if not self.head:
            self.head = self.tail = node(val)
        else:
            self.head.prev = node(val)
            self.head.prev.next = self.head
            self.head = self.head.prev
        self.len += 1
    def print(self):
        temp = self.head
        while temp:
            print(temp.val, end = ' ')
            temp = temp.next
        print()
    def length(self):
        return self.len