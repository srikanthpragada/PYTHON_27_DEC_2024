f = open("employees.txt", "rt")

for line in f.readlines():
    # Remove \n from the line and then split
    parts = line.strip().split(",")
    # first part is dept name
    print(parts[0])

    #list employee names (from second part) in sorted order
    for empname in sorted(parts[1:]):
        print('  ' + empname)

f.close()

