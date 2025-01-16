def wish(*names, message='Hello'):
    for n in names:
        print(message, n)


wish('Mark', 'Scott', 'Jack', "Ben", message='Hi')
wish('Richards', 'David')
