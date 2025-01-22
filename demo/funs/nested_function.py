g = 100  # Global


def f1():
    a = 1  # Enclosing
    global g
    g = 100

    # Nested function / local function
    def f2():
        nonlocal a
        b = 2  # Local
        a = 10
        print('In f2()', g, a, b)

    f2()
    print(a)


f1()
