def DFS_Stack_1(arr, node_name=0):
    # Method 1 is more intuitive and easy to understand
    # Indeed, it's the same as method 2, except for the bigO
    stack = [node_name]  # start
    checked = []#with this method: checked is initially empty, why?
    while stack:
        # Use list to implement Stack
        current_node = stack.pop()
        if current_node not in checked:#because if there is 0 in the checked, then this won't every run!
            checked.append(current_node)
            # Check all adjacent nodes of current_node
            for node, adj_nodes in enumerate(arr):
                if current_node == node:
                    for adj_node, relationship in enumerate(adj_nodes):
                        if adj_node not in stack and adj_node not in checked and relationship == 1:
                            stack.append(adj_node)
    return checked


def DFS_Stack_2(arr, node_name=0):
    stack = [node_name]
    checked = [node_name]
    # implement
    while stack:  # when the stack is not empty
        current_node = stack.pop()
        if current_node not in checked:
                checked.append(current_node)
        for i in range(len(arr[0])):  # traverse through all nodes in each row of the adjacent matrix
            #the beautiful thing here is that i also is the node name :)
            if i not in stack and i not in checked and arr[current_node][i] == 1:
                stack.append(i)
    return checked

    # Use list to store checked nodes


if __name__ == "__main__":
    g1 = [[0, 1, 0, 0, 0, 0, 0],
          [1, 0, 1, 1, 1, 0, 0],
          [0, 1, 0, 0, 0, 1, 0],
          [0, 1, 0, 0, 0, 1, 1],
          [0, 1, 0, 0, 0, 0, 1],
          [0, 0, 1, 1, 0, 0, 0],
          [0, 0, 0, 1, 1, 0, 0]]
    test_1 = DFS_Stack_1(g1)
    test_2 = DFS_Stack_2(g1)
    print(test_1)
    print(f'method 1: {test_1}\n method 2: {test_2}')