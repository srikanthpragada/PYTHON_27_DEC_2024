
f = open("names.txt", "rt")   # Read Text

for name in f.readlines():
    print(name.strip())

f.close()

