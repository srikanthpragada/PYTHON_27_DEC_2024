# Take numbers until 0
# Display all even numbers first and then odd numbers

nums = []

while True:
    n  = int(input("Enter a number [0 to stop] :"))
    if n == 0:
        break
    nums.append(n)

print('Even Numbers :')
for n in nums:
    if n % 2 == 0:
        print(n, end  = ' ')

print('\nOdd Numbers :')
for n in nums:
    if n % 2 != 0:
        print(n, end  = ' ')