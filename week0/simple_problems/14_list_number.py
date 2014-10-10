digits = [1, 2, 3, 5, 7, 8, 6, 1, 2]


def list_digits(arr):
    n = ''
    for i in arr:
        n += str(i)
    return n
print(list_digits(digits))
