def print_table(num, size=10):
    for i in range(1, size + 1):
        print(f"{num:3}  * {i:2} = {i * num:5}")


print_table(15)
print()
print_table(25, 5)
