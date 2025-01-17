# Positional Only
def wish(msg, name, /):
    print(msg, name)


wish('Hello', 'Tom')  # Positional args
#wish(name='Bill', message='Hi')  # Keywords args
