def palindrom(n):
    n = str(n)
    new = ""
    for i in reversed(range(len(n))):
        new += n[i]
    print(new)
    if n == new:
        return "is palindrom"
    else:
        return "it is not a palindrom"
print(palindrom(112211))
