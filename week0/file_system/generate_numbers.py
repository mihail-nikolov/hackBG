import sys
from random import randint


def main():

    file = open(sys.argv[1], "w")
    contents = []
    range_number = int(sys.argv[2])
    for i in range(0, range_number):
        number = randint(1, 10)
        contents.append(str(number))
    file.write(" ".join(contents))
    file.close()

if __name__ == '__main__':
    main()
