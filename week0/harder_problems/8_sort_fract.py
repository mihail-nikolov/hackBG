array = [[4, 3], [1, 2], [2, 3], [3, 8]]


def sort_fract(arr):
    for i in arr:
        for j in arr:
            if j[0] / j[1] < i[0] / i[1]:
                print("da beeeeeeeeeeeeeee")
                tmp = i
                i = [10,10]
                print(i)
                j = tmp
                print(arr)
    #return arr

print(sort_fract(array))
