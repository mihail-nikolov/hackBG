import copy

square = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
for row in square:
    print(row)


def check_sub_results(arr):
    n = arr[0]
    for i in arr:
        if i != n:
            return False
    return n


def sum_rows(matrix):
    result_rows = []
    for row in matrix:
        n = 0
        for el in row:
            n += el
        result_rows.append(n)
    return check_sub_results(result_rows)


def sum_cols(matrix):
    transposed_matrix = copy.deepcopy(matrix)
    transposed_matrix = [list(row) for row in zip(*transposed_matrix)]
    result_rows = []
    for row in transposed_matrix:
        n = 0
        for el in row:
            n += el
        result_rows.append(n)
    return check_sub_results(result_rows)


def sum_diag(matrix):
    n1 = 0
    n2 = 0
    result_diags = []
    for i in range(len(matrix)):
        n1 += matrix[i][i]
    result_diags.append(n1)
    for ind_row in reversed(range(len(matrix))):
        col = abs(i-3)
        n2 += matrix[ind_row][col]
    result_diags.append(n2)
    return check_sub_results(result_diags)


def magic_square(matrix):
    diags = sum_diag(matrix)
    cols = sum_cols(matrix)
    rows = sum_rows(matrix)
    if (rows is False) or (cols is False) or (diags is False):
        return "It is NOT a magic square"
    elif rows == cols and cols == diags:
        return "It is a magic square"

print(magic_square(square))



"""
def sum_cols(matrix):
    result_cols = []
    for column in range(len(matrix[0])):
        n = 0
        for el in matrix:
            n += el[column]
        result_cols.append(n)
    return check_sub_results(result_cols)
"""
