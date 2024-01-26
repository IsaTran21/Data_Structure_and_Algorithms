#Tìm successor của một cây, nếu có 1 child thì + 1 còn không thì + 0
def height_bst(root):
    """root là một kiểu binary search tree"""
    if root is None:
        return 0
    #The base case
    if isLeaf(root):
        return 1


    #Imagine that the height_bst has been already worked
    left = 0
    right = 0
    if root.left:#If it is left child
        left = height_bst(root.left)

    if root.right:
        right = height_bst(root.right)
    if left > right:
        return left + 1
    else:
        return right + 1
def isLeaf(node):
    if node.left is None and node.right is None:
        return True
    else:
        return False