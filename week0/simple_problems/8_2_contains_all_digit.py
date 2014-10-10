digits = [1, 2, 3]
number = 5823791


def contains_digits(n, arr):
    n = str(n)
    for i in n:
        for j in arr:
            if j == int(i):
                arr.remove(j)
    if len(arr) == 0:
        return True
    else:
        return False
print(contains_digits(number, digits))
