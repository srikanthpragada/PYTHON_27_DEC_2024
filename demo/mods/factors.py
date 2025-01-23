# Take a number on command line and display factors
# usage : python factors.py  <number>

import sys

if len(sys.argv) < 2:
    print("Usage : python factors.py  number")
    exit(1)

# Use command-line argument
num =  int(sys.argv[1])

for n in range(2, num // 2 + 1):
    if num % n == 0:
        print(n)

