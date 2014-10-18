array = ["apple", "bottle", "apple", "little", "little", "blqblq"]


def uni_words(arr):
    dictionary = {}
    for i in arr:
        if i not in dictionary:
            dictionary[i] = 1
    return int(len(dictionary))

print(uni_words(array))
