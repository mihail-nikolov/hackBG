def zero_insert(n):
    n = int(n)
    n = str(n)
    new_number = ''
    for i in range(0, len(n)):
        if i == len(n)-1:
            new_number += n[i]
        elif n[i] == n[i+1]:
            new_number += n[i] + '0'
        elif (int(n[i]) + int(n[i+1])) % 10 == 0:
            new_number += n[i] + '0'
        else:
            new_number += n[i]
    return new_number

print(zero_insert(1234655))
