import sys


def main():
    for arg in range(len(sys.argv)):
        file = open(sys.argv[arg], "r")
        content = file.read()
        print(content)

if __name__ == '__main__':
    main()
