string = "Not a Not a Not a NaN"


def it_nan(string):
    string = string.lower()
    not_str = "not a "
    nan_str = "nan"
    last_3 = string[-3:]
    count1 = string.count(not_str)
    count2 = string.count(nan_str)
    if count1 == 0 or count2 != 1 or last_3 != nan_str:
        return False
    else:
        len_str = len(string)
        string = string.replace(nan_str, "")
        for i in range(len_str):
            string = string.replace(not_str, "")
        if len(string) != 0:
            return False
    return count1

print(it_nan(string))
