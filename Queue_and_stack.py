#This module use the Double_linked_list user-defined function
#Create the Interface for Stack and Queue
#This module implement Stack and Queue using user-defined Double_linked_list
from Double_linked_list import Double_linked_list as dll
class IStackQueue:
    def __init__(self):
        self.dll = dll()
    def push(self, data):
        result = self.dll.prepend(data)
        return result
    def pop(self,isStack=False):
        if not isStack:#Then it is queue
            pop_value = self.dll.tail.data#because queue is FIFO
            self.dll.pop()
        else:
            pop_value = self.dll.head.data#because stack is LIFO
            self.dll.remove(0)
        return pop_value
    def isEmpty(self):
        return self.dll.isEmpty()
    def size(self):
        return self.dll.size()
    def top(self, isStack=False):
        if not isStack:#Then it is queue
            return self.dll.tail.data
        else:#Then it is stack
            return self.dll.head.data
    def display(self):
        return self.dll.print()
class Stack(IStackQueue):

    def __init__(self):
        super().__init__()
    def pop(self):
        """pop of stack is the last pushed element"""
        result = super().pop(isStack=True)
        return result
    def top(self):
        """pop of stack is the last pushed element"""
        result = super().top(isStack=True)
        return result
class Queue(IStackQueue):

    def __init__(self):
        super().__init__()
    def pop(self):
        """pop of queue is the first pushed element"""
        result = super().pop()
        return result
    def top(self):
        """pop of queue is the first pushed element"""
        result = super().top()
        return result
if __name__ == "__main__":
    s1 = Stack()
    s1.push(5)
    s1.push(6)
    s1.push(7)
    s1.push(8)
    result = s1.display()
    print(result)
    p1 = s1.pop()
    print(f'After pop {p1}: {s1.display()}')
    p2 = s1.pop()
    print(f'After pop {p2}: {s1.display()}')
    print(f'The top of the stack is {s1.top()}')
    ############################################
    print("TESTING FOR QUEUE")
    print("**************************************************************************************")
    print("**************************************************************************************")
    q1 = Queue()
    q1.push(5)
    q1.push(6)
    q1.push(7)
    q1.push(8)
    result = q1.display()
    print(result)
    qp1 = q1.pop()
    print(f'After pop {qp1}: {q1.display()}')
    qp2 = q1.pop()
    print(f'After pop {qp2}: {q1.display()}')
    print(f'The top of the queue is {q1.top()}')
    q1.pop()
    q1.pop()
    print(q1.isEmpty())


