def sum_of_digits(n):
    n = abs(n)
    intN = int(n)
    if intN == n:
        n = str(n)
        result = 0
        for i in n:
            result = result + int(i)
        return result
    else:
        return False
print(sum_of_digits(123))
