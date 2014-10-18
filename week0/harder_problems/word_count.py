array = ["apple", "bottle", "apple", "little", "little"]


def word_count(arr):
    dictionary = {}
    for i in arr:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    return dictionary

print(word_count(array))
