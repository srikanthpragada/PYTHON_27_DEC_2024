import re

with open("numbers.txt", "r") as f:
    contents = f.read()

nums = re.findall(r"\d+", contents)

for n in sorted(set(map(int, nums))):
    print(n)
