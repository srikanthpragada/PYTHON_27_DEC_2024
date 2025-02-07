from datetime import *

players = []

with open("players.txt", "r") as f:
    for line in f:
        parts = line.split(",")
        # ignore if line doesn't have required details
        if len(parts) < 2:
            continue

        name = parts[0]
        try:
            # convert second part to datetime
            dob = datetime.strptime(parts[1].strip(), "%d-%m-%Y")
        except:
            continue

        days = (datetime.now() - dob).days
        age = days // 365
        players.append((name, age))

# sort by first element of tuple - name
for name, age in sorted(players):
    print(f"{name:15} {age:2}")


# sort by second element of tuple - age
for name, age in sorted(players, key = lambda p : int(p[1])):
    print(f"{name:15} {age:2}")