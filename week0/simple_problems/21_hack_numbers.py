def palindrom(n):
    n = str(n)
    new = ""
    for i in reversed(range(len(n))):
        new += n[i]
    if n == new:
        return True
    else:
        return False


def to_binarry(n):
    n = bin(n)[2:]
    return n


def is_hack(n):
    binar = to_binarry(n)
    binar = str(binar)
    if palindrom(binar) is True:
        empty = ''
        for i in binar:
            if int(i) == 1:
                empty += str(i)
        if len(empty) % 2 == 1:
            return True
    else:
        return False


def next_hack(n):
    for i in range(n+1, 9999999999999999999999999999999999999999):
        if is_hack(i) is True:
            return i

print(next_hack(7918))
