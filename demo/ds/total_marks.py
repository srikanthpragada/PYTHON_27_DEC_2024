
data = "80,45,80,75,50"

marks = data.split(",")
print(marks)

total = 0
for v in marks:
    total += int(v)

print(total)



