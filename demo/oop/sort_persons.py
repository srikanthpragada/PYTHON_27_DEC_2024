class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return  f"{self.name} - {self.age}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    # def __lt__(self, other):
    #     return self.age < other.age

people = [Person("James", 30), Person("Andy", 35), Person("Li", 20)]

for p in sorted(people, key = lambda p : p.name):
    print(p)







