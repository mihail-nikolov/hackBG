def is_number_balanced(n):
    n = int(n)
    n = str(n)
    sum_half1 = 0
    sum_half2 = 0
    #за числа с четен брой цифри

    if len(n) % 2 == 0:
        for i in range(len(n)//2):
            sum_half1 += int(n[i])
        for j in reversed(range(len(n) // 2, len(n))):
            sum_half2 += int(n[j])
    #за числа с нечетен брой цифри

    elif len(n) % 2 == 1:
        for i in range(len(n) // 2):
            sum_half1 += int(n[i])
        for j in reversed(range(len(n) // 2 + 1, len(n))):
            sum_half2 += int(n[j])
    if sum_half1 == sum_half2:
        return "is balanced"
    else:
        return "it is not balanced"

print(is_number_balanced(1234123))


"""def is_number_balanced(n):
    n=int(n)
    n=str(n)
    half1=""
    sum_half1=0
    half2=""
    sum_half2=0
    #за числа с четен брой цифри

    if len(n)%2==0:
        for i in range(len(n)//2):
            half1+=n[i]
            sum_half1+=int(n[i])
        for j in reversed(range(len(n)//2,len(n))):
            half2+=n[j]
            sum_half2+=int(n[j])
    #за числа с нечетен брой цифри  

    elif len(n)%2==1:
        for i in range(len(n)//2):
            half1+=n[i]
            sum_half1+=int(n[i])
        for j in reversed(range(len(n)//2+1,len(n))):
            half2+=n[j]
            sum_half2+=int(n[j])
    print(half1)
    print(sum_half1)
    print(half2)
    print(sum_half2)
    if sum_half1==sum_half2:
        return "is balanced"
    else:
        return "it is not balanced"

print(is_number_balanced(1234567))
"""