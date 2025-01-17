
def isprime(num):
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False

    return True  # prime number


print(isprime(10), isprime(23))

if isprime(47):
    print("Prime")
