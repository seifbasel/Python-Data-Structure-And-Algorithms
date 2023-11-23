class stack:
    def __init__(self):
        self.list = []

    def add(self, data):
        self.list.append(data)

    def pop(self):
        self.list.pop()

    def display(self):
        print(self.list)
        
x = stack()
x.add(3)
x.add(5)
x.add(4)
x.add(9)
x.add(0)
x.display()
x.pop()
x.pop()
x.display()
