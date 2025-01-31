# Generator
def numbers():
    for n in range(1, 10, 2):
        yield  n


g = numbers()
print(type(g))
print(next(g))
print("Next value")
print(next(g))

for n in g:
    print(n)







