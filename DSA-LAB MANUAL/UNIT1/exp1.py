class StackADT:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
        print("Pushed:", value)

    def pop(self):
        if self.isEmpty():
            print("Underflow! Stack is empty.")
            return None
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            print("Stack is empty.")
            return None
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def display(self):
        print("Stack:", self.stack)

s = StackADT()

s.push(10)
s.push(20)
s.push(30)

print("Pop:", s.pop())
print("Peek:", s.peek())
print("Size:", s.size())

s.pop()
s.pop()
s.pop()   # Underflow test

s.display()     