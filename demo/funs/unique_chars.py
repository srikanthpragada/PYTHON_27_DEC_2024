def unique_chars(st1, st2):
    for c in sorted(set(st1) | set(st2)):
        print(c, end='')


unique_chars('java', 'javascript')
