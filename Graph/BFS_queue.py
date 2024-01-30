"""Explores all the neighbors of a node before moving on to the next level of neighbors.
It explores breadth-wise before going deeper.
BFS explores all the neighbors of a node before moving on to the next level of neighbors.
It follows a breadth-wise exploration strategy.
A queue is suitable for BFS because it follows the First-In-First-Out (FIFO) principle.
Nodes are enqueued in the order they are discovered, and the algorithm processes nodes in the order they were added to the queue.
This ensures that BFS explores nodes level by level"""      
# Creating a queue
from queue import Queue
def BFS(arr, node=0):
    queue_ = Queue()
    
    checked = [node]
    queue_.put(node)
    #No need to check whether or not the current_node in queue
    #Because we run leven "top" to "bottom"
    while not queue_.empty():
        current_node = queue_.get()
        for i in range(len(arr)):#because arr is a square matrix
            if i not in checked and arr[current_node][i] == 1:
                checked.append(i)
                queue_.put(i)
    return checked

if __name__ == "__main__":
    g1 = [[0, 1, 0, 0, 0, 0, 0],
          [1, 0, 1, 1, 1, 0, 0],
          [0, 1, 0, 0, 0, 1, 0],
          [0, 1, 0, 0, 0, 1, 1],
          [0, 1, 0, 0, 0, 0, 1],
          [0, 0, 1, 1, 0, 0, 0],
          [0, 0, 0, 1, 1, 0, 0]]
    test_1 = BFS(g1)
    print(test_1)
 
        
