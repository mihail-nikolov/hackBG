def nth_fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return (nth_fibonacci(n - 1) + nth_fibonacci(n - 2))

print(nth_fibonacci(40))



"""

def fib(n):
    p = []
    for i in range(n+1):
        if i == 1 or i == 2:
            p.append(1)
        elif i > 2:
            p.append(p[i-3]+p[i-2])
    fibon = p[len(p)-1]
    return fibon

print(fib(10))
"""
