class All_paths:
    def __init__(self,root):
        self.root = root
        self.paths = []
    def all_paths(self):
        root = self.root
        return self.all_paths_(self.root,"")
    def all_paths_(self,root,result):
        """root is a root of a binary tree"""
        if root is None:
            return None
        #The base case: when we have reached the leaf
        result += str(root.data) + " --> "
        if self.isLeaf(root):
            #result += str(root.data)
            self.paths.append(result)
            return
        left = self.all_paths_(root.left,result)
        right = self.all_paths_(root.right,result)
    
    def isLeaf(self,node):
        """To check if a node is a leaf or not"""
        if node.left is None and node.right is None:
            return True
        else:
            return False
    