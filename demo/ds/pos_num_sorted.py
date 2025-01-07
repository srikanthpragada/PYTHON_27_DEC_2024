# Take numbers until 0
# Display all positive numbers in sorted order

nums = []
while True:
    n  = int(input("Enter a number [0 to stop] :"))
    if n == 0:
        break
    if n > 0:
       nums.append(n)

nums.sort()

for n in nums:
    print(n)



