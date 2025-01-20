def isPositive(n):
    return n > 0

nums = [10, -2, -5, 90,44]

for n in filter(isPositive, nums):
    print(n)

for c in filter( str.isupper , "Python"):
    print(c)

