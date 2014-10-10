array = [1, 2, 3, 6, 7]


def biggest_difference(arr):
    bigg = 0
    for i in arr:
        for j in arr:
            diff = i-j
            if diff > bigg:
                bigg = diff
    return bigg
print(biggest_difference(array))
