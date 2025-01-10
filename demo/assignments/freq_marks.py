data = [80, 70, 85, 80, 70, 50, 60, 80, 85]

marks = {}
for v in set(data):
    marks[v] = data.count(v)


print(marks)