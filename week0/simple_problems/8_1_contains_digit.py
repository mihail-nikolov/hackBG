number = 5823791
n = 2


def contains_digits(n, s):
    n = str(n)
    s = int(s)
    for i in n:
        if int(i) == s:
            return True
    return False
print(contains_digits(number, n))
