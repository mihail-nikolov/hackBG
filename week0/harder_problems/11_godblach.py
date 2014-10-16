def is_prime(x):
    if x > 1:
        if x == 2 or x == 3:
            return True
        else:
            for i in range(2, x - 1):
                if x % i == 0:
                    return False
            return True
    else:
        return False

def goldbach(n):
    arr = []
    for i in range(2, n//2+1):
        if (is_prime(i) is True) and (is_prime(n - i) is True):
            arr.append([i, n - i])
    return arr

print(goldbach(100))
