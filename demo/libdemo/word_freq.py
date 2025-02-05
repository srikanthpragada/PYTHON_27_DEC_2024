import re

# Load data from file
with open("billgates.txt", "rt") as f:
    contents = f.read()

# List of words in the file
words = re.findall(r'\w+', contents)

# Take one word at a time from unique words and display count
for w in sorted(set(words)):
    print(f"{w:15} {words.count(w)}")
