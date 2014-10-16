"""def fib_list(list1, list2, n):
    p = []
    for i in range(n+1):
        if i == 1:
            p.append(list1)
        if i == 2:
            p.append(list2)
        elif i > 2:
            p.append(p[i-3]+p[i-2])
    return p[len(p)-1]

print(fib_list(list_a, list_b, n))
"""