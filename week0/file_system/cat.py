import sys


def main():
    file = open(sys.argv[1], "r")
    content = file.read()
    print(content)
    file.close()

if __name__ == '__main__':
    main()
