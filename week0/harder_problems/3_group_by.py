array = []
for i in range(21):
    array.append(i)


def group_by(an_func, arr):
    dictionary = {}
    for el in arr:
        dictionary.setdefault(an_func(el), []).append(el)
    return dictionary

print(group_by(lambda x: x % 2, array))
print(group_by(lambda x: 'odd' if x % 2 else 'even', array))
print(group_by(lambda x: x % 3, array))
