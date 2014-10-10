string = "Not a Not a Not a NaN"


def it_nan(string):
    not_str = "Not a "
    nan_str = "NaN"
    iteration = string.count(not_str)
    if string.count(nan_str) and iteration > 0:
        answer = iteration
        tot_len = len(nan_str) + answer * len(not_str)
        arr = string.split('')
        print(arr)
        if tot_len != len(arr):
            return False
    else:
        return False
    return answer

print(it_nan(string))

"""def it_nan(string):
    not_str = "Not a "
    nan_str = "NaN"
    tmp = string
    arr = tmp.split(nan_str)
    print(arr)
    arr.pop(len(arr)-1)
    print(len(arr))
    print(arr)
    for i in arr:
        if i == "":
            #защо не трие всичко???!!?!??!?!
            arr.remove(i)
    print(len(arr))
    if len(arr) > 1:
        return False
    #else:
        

it_nan(string)
"""