string = "python"


def count_consonants(n):
    consonant = "bcdfghjklmnpqrstvwxz"
    count = 0
    n = str(n)
    n = n.lower()
    for i in n:
        for j in consonant:
            if i == j:
                count += 1
    return count
print(count_consonants(string))
