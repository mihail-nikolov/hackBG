array = [1, 2, 3, 4, 5]


def inc_seq(arr):
    answer = True
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            answer = False
    return answer
print(inc_seq(array))
