string = "Oython"


def count_vowels(n):
    vowels = "aeiouy"
    count = 0
    n = str(n)
    n = n.lower()
    for i in n:
        for j in vowels:
            if i == j:
                count += 1
    return count
print(count_vowels(string))
