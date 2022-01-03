
class TreeNode:
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None
        
def printsingles(root):
    
    if root is None:
        return
    
    if root.left is not None and root.right is not None:
        printsingles(root.left)
        printsingles(root.right)
        
    elif root.right is not None:
        print(root.right.key)
        printsingles(root.right)
        
    elif root.left is not None:
        print(root.left.key)
        printsingles(root.left)
        
        
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(5)

printsingles(root)