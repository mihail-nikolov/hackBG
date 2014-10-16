square = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]


def check_sub_results(arr):
    n = arr[0]
    for i in arr:
        if i != n:
            return False
    return n

"""
def sumColumn(m, column):
    total = 0
    for row in range(len(m)):
        total += m[row][column]
    return total
"""


def sum_rows(matrix):
    result_rows = []
    n = 0
    for row in matrix:
        for el in row:
            n += el
        result_rows.append(n)
        n = 0
    return check_sub_results(result_rows)


print(sum_rows(square))

#def magic_square(arr):
