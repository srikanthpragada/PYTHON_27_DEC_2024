l = []
for n in range(1, 10):
    l.append(n * n)

print(l)

# List Comprehension
l = [n * n for n in range(1, 10) if n % 2 == 0]
print(l)
