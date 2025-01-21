# We can modify actual parameter using formal parameter for mutable objects

def clear(lst):
    lst.clear()


l = [1, 2, 3]
clear(l)
print(l)
