def wish(message, name):
    print(message, name)


wish('Hello', 'Tom')  # Positional args
wish(name='Bill', message='Hi')  # Keywords args
wish('Hi', name='Mark')  # Mixed
