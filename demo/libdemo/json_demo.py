import json


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(10, 20)

print(p1.__dict__)  # convert object to dict

print(json.dumps(p1.__dict__))
