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


def is_it_works(n):
    if is_prime(n) is True:
        return True
    else:
        for i in range(2, n+1):
            for j in range(1, n+1):
                if (i ** j == n) and (is_prime(i) is True) and (is_prime(j) is True):
                    return True
    return False



def ret_arr(n):
    if is_prime(n) is True:
        arr = [n, 1]
        return arr
    else:
        for c in range(2, n+1):
            for d in range(1, n+1):
                if c ** d == n and (is_prime(c) is True) and (is_prime(d) is True):
                    arr = [c, d]
                    return arr


def prime_fact(n):
    result = []
    if is_prime(n) is True:
        result = [n, 1]
        return result
    else:
        for a in range(2, n+1):
            if n % a == 0:
                for b in range(a, n+1):
                    if (a * b == n) and (is_it_works(a) is True) and (is_it_works(b) is True):
                        arr1 = ret_arr(a)
                        arr2 = ret_arr(b)
                        result = [arr1, arr2]
                        return result
    return False

print(prime_fact(1000))
