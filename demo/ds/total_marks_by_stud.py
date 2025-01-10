data = [(1, 80), (2, 85), (1, 60), (2, 50), (3, 50), (2, 90)]

students = {}
for rollno, marks in data:
    total = students.get(rollno, 0)
    students[rollno] = total + marks

print(students)
