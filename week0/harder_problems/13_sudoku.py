import copy

sudoku_matrix = [
        [4, 5, 2, 3, 8, 9, 7, 1, 6],
        [3, 8, 7, 4, 6, 1, 2, 9, 5],
        [6, 1, 9, 2, 5, 7, 3, 4 ,8],
        [9, 3, 5, 1, 2, 6, 8, 7, 4],
        [7, 6, 4, 9, 3, 8, 5, 2, 1],
        [1, 2, 8, 5, 7, 4, 6, 3, 9],
        [5, 7, 1, 8, 9, 2, 4, 6, 3],
        [8, 9, 6, 7, 4, 3, 1, 5 ,2],
        [2, 4, 3, 6, 1, 5, 9, 8, 7]
]
#square = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
for row in sudoku_matrix:
    print(row)


def check_rows(matrix):
    numbers_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for row in matrix:
        for el in row:
            if el in numbers_array:
                numbers_array.remove(el)
            else:
                return False
        numbers_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return True


def check_cols(matrix):
    transposed_matrix = copy.deepcopy(matrix)
    transposed_matrix = [list(row) for row in zip(*transposed_matrix)]
    numbers_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for row in transposed_matrix:
        for el in row:
            if el in numbers_array:
                numbers_array.remove(el)
            else:
                return False
        numbers_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return True


def make_matrix_3x3(row, col, matrix):
    new_matrix = []
    tmp_matrix = []
    for i in range(row, row+3):
        for j in range(col, col+3):
            tmp_matrix.append(matrix[i][j])
        new_matrix.append(tmp_matrix)
        tmp_matrix = []
    return new_matrix


#numbers_array ?
def check_3x3_matrices(matrix):
    numbers_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for row in matrix:
        for el in row:
            if el in numbers_array:
                numbers_array.remove(el)
                #print(numbers_array)
            else:
                return False
    return True


def sudoku(matrix):
    if (check_cols(matrix) is False) and (check_rows(matrix) is False):
        return "The sudoku is NOT solved 1"
    for i in range(len(matrix)-2):
        for j in range(len(matrix)-2):
            sub_matrix = make_matrix_3x3(i, j, matrix)
            for row in sub_matrix:
                print(row)
            print("------------")
            if check_3x3_matrices(sub_matrix) is False:
                return "The sudoku is NOT solved 2"

    return "The sudoku is solved"

print(sudoku(sudoku_matrix))
