
names = ['Jack', 'Steve', 'Mark', 'Dave']

f = open("names.txt", "wt")   # Write Text

for name in names:
    f.write(name)

f.close()

