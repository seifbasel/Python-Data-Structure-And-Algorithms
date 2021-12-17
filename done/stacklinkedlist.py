class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head
        print('Element of Stack is:[', end='')
        while temp:
            print(temp.data, end=", ")
            temp = temp.next
        print(']')

    def push(self, data):

        if self.head is None:
            self.head = Node(data)
        else:
            temp = Node(data)
            temp.next=self.head
            self.head=temp
        self.display()

    def pop(self):

        if self.head is None:
            print('Stack is Empty')
            return None

        else:
            popped=self.head.data
            self.head=self.head.next
            return popped

    def search(self, search_value):
        node = self.head
        while node != None:
            if node.data == search_value:
                return True
            node = node.next
        return False
    
def main():
    l = Stack()
    print('1.push\n2.pop\n3.exit')
    while 1:
        choice=input('Enter your option:')
        if choice is '1':
            d=int(input('Enter data:'))
            l.push(d)
        elif choice is '2':
            print('poped element is:',l.pop())
            l.display()
        else:
            break
main()



