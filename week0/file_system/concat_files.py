import sys


def main():

    def take_content(arg):
        file = open(arg, "r")
        content = file.read()
        file.close()
        return content

    content = take_content(sys.argv[1]) + take_content(sys.argv[2])

    def put_content(content):
        with open("megatron.txt", "a") as myfile:
            myfile.write(content)

    put_content(content)


if __name__ == '__main__':
    main()
