import re

customers = []
with open("customers.txt", "r") as f:
    for line in f:
        # extract customer name
        m = re.search('[a-zA-Z ]+', line)

        # If name not found, ignore line
        if m is None:
            continue
        else:
            name = m.group(0).strip()

        # extract mobile number
        m = re.search(r'\d+', line)

        # If mobile number not found, ignore line
        if m is None:
            continue
        else:
            mobile = m.group(0)

        customers.append((name, mobile))

for name, mobile in sorted(customers):
    print(f"{name:15} {mobile}")
