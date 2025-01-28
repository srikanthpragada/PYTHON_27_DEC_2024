class Stack:

    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return  self.data.pop()

    @property
    def length(self):
        return len(self.data)

    def clear(self):
        self.data.clear()

    def peek(self):
        return self.data[-1]

s = Stack()
s.push(100)
s.push(200)
print(s.pop())

print(s.length)  # use property

