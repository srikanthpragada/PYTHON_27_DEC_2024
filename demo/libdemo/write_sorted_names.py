# Take names until end is given and write them in sorted order into sorted_names.txt

names = []

while True:
    name = input("Enter name [end to stop] :")
    if name == 'end':
        break

    names.append(name)


with open("sorted_names.txt", "wt") as f:
    for name in sorted(names):
        f.write(name + "\n")

