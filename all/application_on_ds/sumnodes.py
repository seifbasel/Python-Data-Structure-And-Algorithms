class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def haspathsum(node,s):
    ans=0
    subsum=s-node.data
    
    if(subsum == 0 and node.right == None and node.right == None):
        return True
    
    if node.left is not None:
        ans=ans or haspathsum(node.right,subsum)
        
        if node.left is not None:
          ans= ans or haspathsum(node.right, subsum)
    return ans

s=10
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.left.left = TreeNode(5)
if haspathsum(root,s)==0:
    print("false")
else:
    print("true")
