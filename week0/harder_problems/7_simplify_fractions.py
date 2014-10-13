def simp_frac(a, b):
    c = max(a, b)
    for i in reversed(range(1, c + 1)):
        if a % i == 0 and b % i == 0:
            a = a / i
            b = b / i
        arr = [int(a), int(b)]
    return arr

print(simp_frac(3, 9))
