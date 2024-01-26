# Create a Binary Search Tree
# Property of a binary search tree:
# Each node has at most 2 childrens.
# All left descendants of a node contain the values which are always less than the node itself.
# All right descendants of a node contain the values which are always greater than the node itself.
class TreeNode:
    # just like linked list, instead of head and tail, here are the left and right
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value, node):
        if node is None:
            self.root = TreeNode(value)
            return
        if value < node.data:
            if node.left is None:
                node.left = TreeNode(value)
            self.insert(value, node.left)
        elif value > node.data:
            if node.right is None:
                node.right = TreeNode(value)
            self.insert(value, node.right)
    def insert_loop(self,value, node):
        if node is None:
            self.root = TreeNode(value)
            return
        while True:
            if value < node.data:
                if node.left is None:
                    node.left = TreeNode(value)
                    break
                else:
                    node = node.left
            else:#value > node.data:
                if node.right is None:
                    node.right = TreeNode(value)
                    break
                else:
                    node = node.right
    def search(self, value, node)->bool:
        while node:
            if value == node.data:
                return True
            if value < node.data:
                node = node.left
            else:
                node = node.right
        else:
            return False
                    

    def traverse(self, node):
        if node is None:
            return
        self.traverse(node.left)
        print(node.data)
        self.traverse(node.right)


    def remove(self, value, node):
        #The base case is the bottom of the tree
        if node is None:
            return None
        elif value < node.data:
            node.left = self.remove(value, node.left)
            return node
        elif value > node.data:
            node.right = self.remove(value, node.right)
            return node
        elif value == node.data:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                node.right = self.replace(node.right, node)
                return node
    def replace(self,node,node_to_delete):
        if node.left:
            node.left = self.replace(node.left, node_to_delete)
            return node
        else:
            node_to_delete.data = node.data
            return node.right
if __name__ == "__main__":
    # Testing the TreeNode first (use debug)

    # root = TreeNode(10)
    #t1 = BST()
    #t1.insert(11, t1.root)
    #t1.insert(9, t1.root)
    #t1.insert(12, t1.root)
    #t1.insert(13, t1.root)
    #t1.insert(14, t1.root)
    #t1.insert(15, t1.root)
    #t1.traverse(t1.root)
    
    t2 = BST()
    t2.insert_loop(8, t2.root)
    t2.insert_loop(3, t2.root)
    t2.insert_loop(10, t2.root)
    t2.insert_loop(1, t2.root)
    t2.insert_loop(6, t2.root)
    t2.insert_loop(14, t2.root)
    t2.insert_loop(4, t2.root)
    t2.insert_loop(7, t2.root)
    t2.insert_loop(13, t2.root)
    t2.remove(6, t2.root)
    t2.traverse(t2.root)

