string = "ispismisvisthis his cis"
substr = "is"


def count_substrings(st, sub):
    if len(st) < len(sub):
        return False
    count = 0
    tmp = ''
    for i in range(len(st)):
        if st[i] == sub[0]:
            for j in range(i, i + len(sub)):
                tmp += st[j]
            if tmp == sub:
                count += 1
            tmp = ''
    return count
print(count_substrings(string, substr))
