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
print(is_prime(101))
