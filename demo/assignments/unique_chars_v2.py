
names = ['java', 'javascript', 'c#', 'python', 'sql']

chars = set()
for n in names:
    chars = chars | set(n)

print(chars)
