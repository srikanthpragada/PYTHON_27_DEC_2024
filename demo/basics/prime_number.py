# Take a number and display whether it is prime number

num = int(input("Enter a number :"))

prime = True   # Flag

for n in range(2, num // 2 + 1):
    if num % n == 0:
         print('Not a prime number')
         prime = False
         break

if prime:
    print("Prime number")



