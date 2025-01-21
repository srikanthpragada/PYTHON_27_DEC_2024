def isprime(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False

    return True  # prime number


nums = [123, 35, 37, 23, 88]

for n in filter(isprime, nums):
    print(n)
