class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None
    
    def enquque(self,data):
        if self.head==None:
            newnode=Node(data)
            self.head=newnode
            self.tail=self.head
        else:
            newnode = Node(data)
            self.tail.next=newnode
            self.tail=newnode
            
    def dequeue(self):
        data = self.head.data
        self.head = self.head.next
        if self.head == None:
            self.last = None
        return data
         
    def display(self):
        current = self.head
        while current != None:
                print(current.data, end=" ")
                current = current.next

q =Queue()
q.enquque(10)
q.enquque(20)
q.enquque(30)
q.enquque(40)
q.enquque(50)
q.enquque(60)
q.enquque(70)
q.dequeue()
q.dequeue()
q.dequeue()
q.display()
print(q.isEmpty())
print("Queue Front " + str(q.head.data))
print("Queue Rear " + str(q.tail.data))
