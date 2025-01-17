
def upper_count(st):
    count = 0
    for c in st:
        if c.isupper():
            count += 1

    return count


print(upper_count('How Are You'))
