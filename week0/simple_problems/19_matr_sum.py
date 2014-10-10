matrix = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]


def matr_sum(m):
    result = 0
    for li in m:
        for n in li:
            result = result + n
    return result
print(matr_sum(matrix))
