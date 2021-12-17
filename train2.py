class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
    def insert(self,data):
        if self.data==None:
            self.data=data
        else:
            if data<self.data:
                if self.left==None:
                    self.left=node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = node(data)
                else:
                    self.right.insert(data)


    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()


root=node(0)
root.insert(1)
root.insert(2)
root.PrintTree()
root.insert(3)
root.insert(4)
root.PrintTree()
