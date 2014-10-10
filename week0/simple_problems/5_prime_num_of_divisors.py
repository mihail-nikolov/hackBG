def is_prime(x):
    if x > 1:
        if x == 2 or x == 3:
            return True
        else:
            for i in range(2, x-1):
                if x % i == 0:
                    return False
            return True
    else:
        return False


def prime_number_of_divisors(n):
    result = 0
    for i in range(1, n+1):
        if n % i == 0:
            result += 1
    print(result)
    return is_prime(result)
print(prime_number_of_divisors(8))
