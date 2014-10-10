times = 2


def nan_exp(t):
    not_str = 'Not a '
    end_str = 'NaN'
    string = ''
    for i in (0, t):
        if i == t:
            string += not_str + end_str
        else:
            string += not_str
    return string
print(nan_exp(times))
