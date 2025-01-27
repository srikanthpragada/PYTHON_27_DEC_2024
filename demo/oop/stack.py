class Stack:

    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return  self.data.pop()

    def length(self):
        return len(self.data)

    def clear(self):
        self.data.clear()



s = Stack()
s.push(100)
s.push(200)

print(s.pop())
print(s.length())

