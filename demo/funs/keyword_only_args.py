# Keyword-only args
def wish(*, name, message):
    print(message, name)

wish(name='Bill', message='Hi')  # Keywords args
#wish("Hello", "Jack")


