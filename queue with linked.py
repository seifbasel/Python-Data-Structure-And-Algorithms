class Queue:

 class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        if self.head == None:
            node = self.Node(data)
            self.head = node
            self.tail = self.head
        else:
            node = self.Node(data)
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
            print(current.data, end=" ")
            current = current.next
