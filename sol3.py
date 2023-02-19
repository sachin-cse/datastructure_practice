class Stack:

    def __init__(self):
        self.stack = []
        self.max_value = 0

    def push(self,item):
        self.stack.append(item)
        self.max_value = max(self.max_value, item)

    def pop(self, item):
        if self.stack is None:
            print("stack is underflow")
        else:
            return self.stack.pop()

    def get_length(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None



stack = Stack()
stack.push(1)
stack.push(6)
stack.push(5)
stack.push(4)

print("Stack:", stack.stack)
print("Maximum Value in Stack:", stack.max_value)
