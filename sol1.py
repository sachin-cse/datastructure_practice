class Node:
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = next
    
class Linkedlist:
    def __init__(self):
        self.head = None

    # insert at begining
    def insert_at_begining(self,data):
        node = Node(data, self.head)
        self.head = node

    # print data
    def printlist(self):
        current = self.head
        while current:
            print(current.data, end = "\n")
            current = current.next

    # middle element
    def find_middle(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    # reverse linked list
    def reverse_list(self):
        prev = None
        curr = self.head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    # print data in reverse order
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
    
    # get length
    def get_length(self):
        count=0
        temp = self.head
        while temp!=None:
            count+=1
            temp = temp.next
        return count

    # has cycle
    def has_cycle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False

    
        


l = Linkedlist()
l.insert_at_begining(2)
l.insert_at_begining(3)
l.insert_at_begining(4)
l.insert_at_begining(5)
l.printlist()
print(l.get_length())
print(l.has_cycle())
# print(l.find_middle())
# l.reverse_list()
# l.print_list()


