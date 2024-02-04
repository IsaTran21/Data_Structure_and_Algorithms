class Distra:
    def __init__(self,arr, start, finish=None):
        #arr is an adjacent_matrix
        #start is the starting node
        self.finish = finish#the node needed to find the shortest distance
        self.arr = arr
        self.start = start
        self.parents = None
        self.distance = None
    def dijstra(self):
        
        import math
        # Defining a positive infinite integer
        inf = math.inf
        
        #Set up: step 1
        #distance table
        distance = [inf for i in range(len(self.arr))]
        #parent table
        parent = [None for i in range(len(self.arr))]
        distance[self.start] = 0
        #print(distance)
        visited = []
        while len(visited) < len(self.arr):#each row is a node
            #step 2: find current node (shortest distance)
            min_distance = inf
            
            for i in range(len(distance)):#the index is already the node name
                if i not in visited and distance[i] < min_distance:
                    current = i
                    min_distance = distance[i]
                    
            #step 3: find all neighbours and update disntace
            for j in range(len(self.arr)):#because arr is a square matrix - use j to indicate "inner loop"
                if j not in visited and self.arr[current][j] != 0:# a neighbour must != 0
                    new_distance = self.arr[current][j] + distance[current] #the distance between the current node and
                    #its neighbour + the distance from the root to that current node
                    if new_distance < distance[j]:#each node has a distance from the root (culmulative distance)
                        distance[j] = new_distance
                        parent[j] = current
            visited.append(current)
        self.distance = distance
        self.parents = parent
        #return distance, parent
    def path(self):
        self.dijstra()
        path = []
        if self.finish is not None:
            node = self.finish
            while node != self.start:
                path.insert(0,node)
                node = self.parents[node]
            path.insert(0,self.start)
        return path
    def shortest_distance(self):
        self.dijstra()
        return f'The shortest distance from {self.start} to {self.finish} is {self.distance[self.finish]}'
        

if __name__ == "__main__":
    arr = [
        [0,6,0,1,0],
        [6,0,5,2,2],
        [0,5,0,0,5],
        [1,2,0,0,1],
        [0,2,5,1,0]
    ]
    #start = 0
    #dijstra(arr,0)
    start = 0
    finish = 2
    test_1 = Distra(arr,0,2)
    path = test_1.path()
    distance = test_1.shortest_distance()
    print(path)
    
    print(distance)
    arr_1 = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]
    

    test_2 = Distra(arr_1,0,5)
    path = test_2.path()
    distance = test_2.shortest_distance()
    print(path)
    print(distance)