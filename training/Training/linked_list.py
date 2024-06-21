class node:
    def __init__(self, value):
        self.val = value
        self.next = None
class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def append(self, val):
        if self.head:
            new_node = node(val)
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = self.tail = node(val)
        self.length += 1
    def pop(self):
        if self.head == self.tail:
            self.head = self.tail = None
        if self.head:
            val = self.tail.val
            temp = self.head
            while temp.next.next:
                temp = temp.next
            temp.next = None
            self.tail = temp
            self.length -= 1
            return val
        else:
            return 'Empty List'
    def print(self):
        if self.head:
            temp = self.head
            while temp.next:
                print(temp.val, end = ' ')
                temp = temp.next
            print(self.tail.val)
        else:
            print('Empty List')
    def len(self):
        return self.length
    def find(self, val):
        temp = self.head
        while temp:
            if temp.val == val:
                return True
            temp = temp.next
        return False
    def mid(self):
        if not self.head:
            return 'Empty List'
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.val
    def even_or_odd(self):
        fast = self.head
        while fast and fast.next:
            fast = fast.next.next
        if fast:
            return 'Odd'
        return 'Even'
    def add_at_front(self, val):
        new_node = node(val)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = self.tail = new_node
    def delete_at_front(self):
        if not self.head:
            return 'Empty List'
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            val = self.head
            self.head = self.head.next
            return val
    def max_length_of_sequence(self):
        if not self.head:
            return 0
        max_length = length = 1
        temp = self.head
        while temp.next:
            if temp.val + 1 == temp.next.val:
                length += 1
            else:
                max_length = max(max_length, length)
                length = 1
            temp = temp.next
        return max(max_length, length)
    def pairs(self):
        temp = self.head
        while temp.next:
            temp1 = temp.next
            while temp1:
                print((temp.val,temp1.val))
                temp1 = temp1.next
            temp = temp.next
a = List()
a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.append(7)
a.append(8)
a.append(9)
a.append(3)
a.append(4)
a.append(5)
a.print()
a.pairs()