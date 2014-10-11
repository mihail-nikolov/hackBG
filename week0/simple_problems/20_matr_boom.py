import copy

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def matrix_boom(i, j, val,  matrix):
    new_matrix = copy.deepcopy(matrix)
    for row_i, row in enumerate(new_matrix):
            if row_i == i or row_i == i - 1 or row_i == i + 1:
                for column_j, number in enumerate(row):
                    if column_j == j - 1 or column_j == j + 1 or column_j == j:
                        if column_j == j and row_i == i:
                            row[column_j] = val
                        else:
                            number -= val
                            if number < 0:
                                row[column_j] = 0
                            else:
                                row[column_j] -= val
    return new_matrix


def matrix_sum(matrix):
    result = 0
    for row in matrix:
        for number in row:
            result += number
    return result


def matr_boom_plan(matrix):
    dic = {}
    for row_i, row in enumerate(matrix):
        for column_j, num in enumerate(row):
            index = "(" + str(row_i) + "," + str(column_j) + ")"
            boomed_matrix = matrix_boom(row_i, column_j, num, matrix)
            result = matrix_sum(boomed_matrix)
            dic[index] = result
            index = ""
    return dic

print(matr_boom_plan(matrix))
