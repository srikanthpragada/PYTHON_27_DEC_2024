names = []  # empty list

while True:
    name = input("Enter name [end to stop] :")
    if name == 'end':
        break

    names.append(name)

# Print names in reverse order
for n in names[::-1]:
    print(n)
