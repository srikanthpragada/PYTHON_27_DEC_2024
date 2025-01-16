
names = {}

while True:
    name = input("Enter name [end to stop] :")
    if name == 'end':
        break

    count = names.get(name, 0)
    names[name] = count + 1


#print(names)
for name in sorted(names.keys()):
    count = names[name]
    print(f"{name:10}  {count:3}")



