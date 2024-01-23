class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
class Double_linked_list:
    """index starts at 0"""
    def __init__(self):
        self.head = None #First initialize the object
        self.tail = None
    def append(self, data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
            return
        new_node = Node(data, next=None, prev=self.tail)
        self.tail.next = new_node
        self.tail = new_node

    def prepend(self, data):
        """append to the head of the linked list"""
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node
            return
        new_node = Node(data, next=self.head)
        self.head.prev = new_node
        self.head = new_node
    def print(self):
        """from left to right"""
        current = self.head
        result = ""
        while current:
            result += str(current.data) + "-->"
            current = current.next
        return result
    def print_reverse(self):
        """from right to left"""
        current = self.tail
        result = ""
        while current:
            result += str(current.data) + "-->"
            current = current.prev
        #for i in
        return result
    def insert_after(self, data, index):
        """insert after index-th position"""
        position = 1
        current = self.head
        if self.size() < index:
            return "Out of range"
        while position <= index:
            position += 1
            current = current.next
        new_node = Node(data, prev=current, next = current.next)
        current.next = new_node
    def insert_before(self, data, index):
        """insert after index-th position"""
        position = 2
        current = self.head
        if self.size() < index:
            return "Out of range"
        while position <= index:
            position += 1
            current = current.next
        new_node = Node(data, prev=current, next = current.next)
        current.next = new_node
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next

        return count
    def remove(self, index):
        if self.head == None:
            return "Nothing to remove"
        if index == 0:
            current = self.head
            #Remove the first node
            current.next = current
            current.pre = None
            return
        if index > self.size():
            print("Out of range")
            return
        if index == self.size():
            current = self.head
            while current.next.next:#The next of the next of the current is None
                #It means that the current.next is not None => remove the current.next
                current = current.next
            current.next = None
            return
        current = self.head
        position = 1
        while position < index:
            position += 1
            current = current.next
        current.next.next.prev = current
        current.next = current.next.next



o1 = Double_linked_list()
o1.append(1)
o1.append(2)
o1.append(3)
o1.prepend(9)
a = o1.print()
b = o1.print_reverse()
print(f'Print forward: {a}')
print(f'Print backward {b}')
o2 = Double_linked_list()
print(f'Is o1 empty {o1.isEmpty()}\nIs o2 empty {o2.isEmpty()}')
print(f"The size of o1 is {o1.size()}\nThe size of o2 is {o2.size()}")
print(f'Before inserting after index 2: {o1.print()}')
o1.insert_after(10, 2)
print(f'After inserting after index 2: {o1.print()}')
o1.insert_before(10, 2)
print(f'After inserting before index 2: {o1.print()}')
o1.remove(2)
print(f'After removing at index 2 is: {o1.print()}')
o1.remove(12)