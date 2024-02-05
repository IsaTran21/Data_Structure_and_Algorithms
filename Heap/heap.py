#heap = binary tree + heap property
#types: max heap (parent >= children) and min heap (parent <= children)
#Save in memory: linear array because of continuous indices
#Heap operations:
#isEmpty, peek, add, poll, remove, remove a specific node,
#heapify up and down: to maintain the heap property when add or remove node
class Heap:
    
    def __init__(self, size):
        self.size = size #size is the numbers of elemnts in the heap
        self.arr = [0 for i in range(size)] # to store each element
        #the size is also the index of the last element in the heap!
        
    def parent_index(self, index):
        if index == 0 or len(self.arr) == 1 or len(self.arr) == 0 or index > self.size:
            return -1#if index 0 or the heap is empty or has only 1 node or the index is greater than the size => no parent!
        else:
            return (index - 1) // 2
        
    def leftchild_index(self, index):
        if index * 2 + 1 <= self.size - 1:
            return index * 2 + 1
        else:
            return self.size + 1#just for the condition below when removing
        
    def rightchild_index(self, index):
        if index * 2 + 2 <= self.size - 1:
            return index * 2 + 2
        else:
            return self.size + 1#just for the condition below when removing
    
    def isEmpty(self):
        if len(self.arr) == 0:
            return True
        else:
            return False
    def add(self, value):
        self.arr.append(value)#add the value at the end of the array
        self.size += 1#increase the size of the array to 1
        #must ensure the heap property
        self.heapify_up()
    def heapify_up(self):
        #use for add
        current_index = self.size - 1#the last element - because Python starts with 0!
        while (self.parent_index(current_index) >= 0):#stop when the current_index points to the root => it has no parent
            if self.arr[current_index] < self.arr[self.parent_index(current_index)]:
                self.swap(current_index, self.parent_index(current_index), self.arr)#swap value
                current_index = self.parent_index(current_index)#move the pointer up up up, one node up at the time
            else:
                break #the heap property is satisfied
            
    def heapify_down(self, index=0):
        #used for remove
        #choose the child with the smallest value then swap
        #stop when the heap property is already satisfy
        current_index = index
        while self.leftchild_index(current_index) <= self.size - 1:#no need to check the right, because of the heap property
            #choose the child with the smallest value
            min_index = self.leftchild_index(current_index)
            min_child = self.arr[min_index]
            if self.rightchild_index(current_index) < self.size - 1:#if there is a right child of the current index
                right_child = self.arr[self.rightchild_index(current_index)]
                if right_child < min_child:
                    min_index = self.rightchild_index(current_index)
                    min_child = right_child
            #compare and swap if any
            if self.arr[current_index] > min_child:
                self.swap(current_index, min_index, self.arr)
                current_index = min_index
            else:
                break

        
    def remove(self, value):
        #Find the index of the value if exists
        if len(self.arr) == 0:
            return
        current_index = None
        for i in range(len(self.arr)):
            if self.arr[i] == value:
                current_index = i
        if current_index is None:
            return
        else:
            self.arr[current_index] = self.arr[len(self.arr) - 1]
            self.arr = self.arr[0:len(self.arr) - 1]
            self.size = len(self.arr)
            self.heapify_down(index=current_index)
        
    def remove_root(self):
        if len(self.arr) == 0:
            return
        self.arr[0] = self.arr[len(self.arr) - 1]
        self.arr = self.arr[0:len(self.arr) - 1]
        self.size = len(self.arr)
        self.heapify_down()
    def swap(self, i, j, arr):
        #Use for swapping the value, not the index! must be clear that this function only swap value between the two element
        #with its corresponding index in the array named arr!
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
if __name__ == "__main__":
    o1 = Heap(0)
    o1.add(10)
    o1.add(20)
    o1.add(5)
    o1.add(8)
    o1.add(0)
    #o1.add(3)
    
    print(o1.arr)
    
    o1.remove_root()
    print(o1.arr)
    #o1.remove_root()
    #print(o1.arr)
    #o1.remove_root()
    #print(o1.arr)
    #o1.remove_root()
    #print(o1.arr)
    #o1.remove_root()
    #print(o1.arr)
    o1.remove(10)
    print(o1.arr)
    o1.remove(8)
    print(o1.arr)
    o1.remove(20)
    print(o1.arr)
    #o1.remove(5)
    #print(o1.arr)
    o1.remove(15)
    print(o1.arr)
