class queue:
    def __init__(self):
        self.queue=[]
    
    def add(self,value):
        self.queue.append(value)
    
    def show(self):
        print(self.queue)
        
    def pop(self):
        self.queue.pop()
        
x=queue()
x.add(1)

x.add(3)
x.add(4)
x.add(5)
x.show()
x.pop()
x.pop()
x.show()
