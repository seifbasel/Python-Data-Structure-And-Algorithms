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
    
    def enqueue(self, data):
        if self.head == None:
            node = Node(data)
            self.head = node
            self.tail = self.head
        else:
            node =Node(data)
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        data = self.head.data
        self.head = self.head.next
        if self.head == None:
            self.last = None
        return data

    def display(self):
        current = self.head
        while current != None:
            print(current.data, "\n ")
            current = current.next


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
q.enqueue(70)
q.dequeue()
q.dequeue()
q.dequeue()
q.display()
print(q.isEmpty())
print("Queue Front " + str(q.head.data))
print("Queue Rear " + str(q.tail.data))
