names = ['Java', 'python', 'SQL', 'c']


def first3(n):
    return n[:3]


for n in map(first3, names):
    print(n)

for n in map(lambda n : n[:3], names):
    print(n)
