f = open("marks.txt", "rt")

for line in f.readlines():
    parts = line.split(',')
    if len(parts) < 2:  # maybe blank line or missing data, so ignore it
        continue

    name = parts[0]
    total = sum(map(int, parts[1:]))
    print(f"{name:15}  {total:3}")

f.close()
