# Take a number and display factors

num = int(input("Enter a number :"))

for n in range(2, num // 2):
    if num % n == 0:
        print(n)

