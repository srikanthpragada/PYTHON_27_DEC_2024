def hasupper(st):
    """
    Returns true if string contains an uppercase letter
    :param st: string to examine
    :return: True if uppercase if found otherwise false
    """
    for c in st:
        if c.isupper():
            return True

    return False


def countupper(st):
    count = 0
    for c in st:
        if c.isupper():
            count += 1

    return count
