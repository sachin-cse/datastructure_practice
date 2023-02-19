class Node:
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = next
    
class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        node = Node(data, self.head)
        self.head = node


    def delete_node(self,target):
        current = self.head
        if current.data == target:
            return current.next
        while current.next:
            if current.next.data == target:
                current.next = current.next.next
                return self.head
            current = current.next
        return self.head

    def printlist(self):
        current = self.head
        while current:
            print(current.data, end = "\n")
            current = current.next



l = Linkedlist()
l.insert_at_begining(2)
l.insert_at_begining(3)
l.insert_at_begining(4)
l.printlist()
l.delete_node(2)
