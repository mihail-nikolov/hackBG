array = [[4, 3], [1, 2], [2, 3], [3, 8]]


def sort_fract(arr):
    for i, el_i in enumerate(arr):
        for j, el_j in enumerate(arr):
            if el_j[0] / el_j[1] > el_i[0] / el_i[1]:
                tmp = arr[j]
                arr[j] = arr[i]
                arr[i] = tmp
                print(arr)
    return arr

print(sort_fract(array))
