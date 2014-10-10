array = [5, 6, 3, 2, 1]


def dec_seq(arr):
    answer = True
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            answer = False
    return answer
print(dec_seq(array))
