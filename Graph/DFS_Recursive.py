def DFS_recursive(arr,current_node,checked):
    #print(current_node)
    #The base case: when there is no 
    for i in range(len(arr)):#because it's a square matrix
        if arr[current_node][i] == 1 and i not in checked:
            checked.append(i)
            DFS_recursive(arr, i, checked)
    return checked

def DFS_recursive_result_like_stack(arr,current_node,checked):
    #print(current_node)
    #print(current_node)
    #The base case: when there is no 
    for i in range(len(arr)-1,-1,-1):#because it's a square matrix
        if arr[current_node][i] == 1 and i not in checked:
            checked.append(i)
            DFS_recursive_result_like_stack(arr, i, checked)
    return checked
if __name__ == "__main__":
    g1 = [[0, 1, 0, 0, 0, 0, 0],
          [1, 0, 1, 1, 1, 0, 0],
          [0, 1, 0, 0, 0, 1, 0],
          [0, 1, 0, 0, 0, 1, 1],
          [0, 1, 0, 0, 0, 0, 1],
          [0, 0, 1, 1, 0, 0, 0],
          [0, 0, 0, 1, 1, 0, 0]]
    #checked = []

    test_1 = DFS_recursive(g1,0,[0])
    
    #print(test_1)
    print(f'method 1: {test_1}')

    test_2 = DFS_recursive_result_like_stack(g1,0,[0])

    #print(test_1)
    print(f'DFS_recursive_result_like_stack: {test_2}')
