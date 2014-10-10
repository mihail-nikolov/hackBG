array = ["apple", "bottle", "apple", "little", "little"]


def uni_words(arr):
    dictionary = {}
    print(dictionary)
    for i in arr:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    return len(dictionary)       
print(uni_words(array))
