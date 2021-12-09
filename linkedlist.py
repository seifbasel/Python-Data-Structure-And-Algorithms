class Node:
    def __init__(self,data):
        self.dataval=data
        self.next=None
        
class linkedlist:
    def __init__(self):
        self.head=None
    
    def add(self,newdata):
        newnode=Node(newdata)
        newnode.next=self.head
        self.head=newnode
        
    def show(self):
        node=self.head
        while node is not None:
            print(node.dataval)
            node=node.next

    def search(self, x):

        # Initialize current to head
        current = self.head

        # loop till current not equal to None
        while current != None:
            if current.dataval == x:
                return True  # data found

            current = current.next

        return False  # Data Not found
        
list_1=linkedlist()
list_1.add(1)
list_1.add(2)
list_1.add(3)
list_1.add(4)

list_1.show()

if list_1.search(4):
    print("Yes")
else:
    print("No")
