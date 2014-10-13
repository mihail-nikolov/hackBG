array = [1, 2, 3, 7, 7, 8, 8, 7, 7, 7, 7]
n=5


def sevens_in_a_row(arr, n):
    count = 0
    for i in range(len(arr)):
        if arr[i] == 7:
            for j in range(i + 1, i + n):
                if j == len(arr):
                    break
                elif arr[j] == 7:
                    count = count + 1
            if (count + 1) == n:
                return True
            else:
                count = 0
    return False
print(sevens_in_a_row(array, n))

"""array=[1,2,3,7,7,8,8,7,7,7,7]
n=5
def sevens_in_a_row(arr, n):
    for i in range(len(arr)):
        if arr[i]==7:
            for j in range(i+1,i+n):
                if j==len(arr):
                    break
                elif arr[j]!=7:
                    break

            print(True) 
    return False
print(sevens_in_a_row(array, n))"""