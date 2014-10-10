def calc_coins(n):
    arr = [100, 50, 20, 10, 5, 2, 1]
    cost = {'100': 0, '50': 0, '20': 0, '10': 0, '5': 0, '2': 0, '1': 0}
    n = n * 100
    n = int(n)
    while n > 0:
        for i in arr:
            if n - i >= 0:
                n = n - i
                i = str(i)
                cost[i] = cost[i] + 1
                break
    return cost

print(calc_coins(5.83))
