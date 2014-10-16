import copy


sudoku = [
        [4, 5, 2, 3, 8, 9, 7, 1, 6], [3, 8, 7, 4, 6, 1, 2, 9, 5], [6, 1, 9, 2, 5, 7, 3, 4 ,8],
        [9, 3, 5, 1, 2, 6, 8, 7, 4], [7, 6, 4, 9, 3, 8, 5, 2, 1], [1, 2, 8, 5, 7, 4, 6, 3, 9],
        [5, 7, 1, 8, 9, 2, 4, 6, 3], [8, 9, 6, 7, 4, 3, 1, 5 ,2], [2, 4, 3, 6, 1, 5, 9, 8, 7]
]
for row in sudoku:
    print(row)

print([list(row) for row in zip(*sudoku)])



def check_rows(matrix):
    numbers_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for row in matrix:
        for el in row:
            if el in numbers_array:
                sub_arr.remove(el)
            else:
                return False
        numbers_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    return True


def check_cols(matrix):
    for column in range(len(matrix[0])):
        n = 0
        for row in matrix:
            n += row[column]
        result_cols.append(n)
    return check_sub_results(result_cols)

"""
def check_sub_results(arr):
    n = arr[0]
    for i in arr:
        if i != n:
            return False
    return n








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