def list_digits(n):
    n = int(n)
    n = str(n)
    digits = []
    for i in n:
        digits.append(int(i))
    return digits
print(list_digits(5164865))
