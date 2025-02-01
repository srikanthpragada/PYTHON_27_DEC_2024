def factors(num):
    for n in range(2, num // 2 + 1):
        if num % n == 0:
            yield  n


for v in factors(124):
    print(v)

