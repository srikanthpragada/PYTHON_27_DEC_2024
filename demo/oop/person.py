class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return  f"{self.name} - {self.age}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __gt__(self, other):
        return self.age > other.age

p1 = Person("James", 30)
p2 = Person("Andy", 35)
p3 = Person("James", 30)

print(p1)  # str(p1)  ->  p1.__str__()
print(str(p1))
print(p1 == p3)   # p1.__eq__(p3)
print(p1 == p2)   # p1.__eq__(p3)
print(p2 > p1)    # p2.__gt__(p1)
print(p2 < p3)    # p2.__gt__(p1)





