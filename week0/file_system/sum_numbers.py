import sys
from random import randint


def main():

    def sum_int(arr):
        result = 0
        for el in arr:
            result += int(el)
        return result

    def read_file():
        file = open(sys.argv[1], "r")
        content = file.read()
        arr = content.split(" ")
        file.close()
        return arr

    arr = read_file()
    print(sum_int(arr))

if __name__ == '__main__':
    main()
