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
        #
        self.tail = new_node
        self.tail.prev.next = new_node

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
        position = 0
        current = self.head
        if self.size() < index:
            return "Out of range"
        while position < index:
            position += 1
            current = current.next
        new_node = Node(data, prev=current, next = current.next)
        #current.next = new_node

        if current.next:
            current.next.prev = new_node
        current.next = new_node
        #If isnert at the end of the linked list
        if new_node.next is None:
            self.tail = new_node
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
    def pop(self):
        index = self.size() - 1
        pop = self.tail.data
        self.remove(index)

        return pop
    def remove(self, index):
        if self.head == None:
            return "Nothing to remove"
        if index == 0:
            if self.size() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
            return
        if index >= self.size():
            print("Out of range")
            return

        if index == self.size() - 1:
            current = self.tail.prev
            self.tail = current
            self.tail.next = None

            return

        current = self.head
        position = 0
        while position < index:
            position += 1
            current = current.next
        current.prev.next = current.next
        current.next.prev = current.prev


if __name__ == "__main__":
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
    o1.insert_before(8, 2)
    print(f'After inserting before index 2: {o1.print()}')
    o1.remove(2)
    print(f'After removing at index 2 is: {o1.print()}')
    o1.remove(12)
    print(f"o1 before removing is {o1.print()}")
    o1.remove(0)
    print(f"o1 after removing at front: {o1.print()}")
    o1.remove(3)
    print(f"o1 after removing at ending: {o1.print()}")
    o1.remove(4)
    print(f"o1 after removing at 1: {o1.print()}")
    result = o1.pop()
    print(f"o1 after popping: {o1.print()}, pop value = {result}")
    result = o1.pop()
    print(f"o1 after popping: {o1.print()}, pop value = {result}")