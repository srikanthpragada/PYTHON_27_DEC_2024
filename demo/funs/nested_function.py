g = 100  # Global


def f1():
    a = 1  # Enclosing

    # Nested function / local function
    def f2():
        b = 2  # Local
        a = 10
        print('In f2()', g, a, b)

    f2()
    print(a)

f1()
