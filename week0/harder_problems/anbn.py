word = 'aaabbb'


def is_an_bn(w):
    if len(w) % 2 == 1:
        return False
    else:
        middle = int(len(w) / 2)
        w = w.lower()
        for i in range(middle):
            if w[i] != 'a':
                return False
        for j in range(middle, len(w)):
            if w[j] != 'b':
                return False
    return True

print(is_an_bn(word))
