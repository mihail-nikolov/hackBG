import sys
from random import randint


def main():

    def read_file(n):
        file = open(sys.argv[n], "r")
        content = file.read()
        file.close()
        return content

    def chars_command(string):
        result = 0
        for char in string:
            result += 1
        return result

    def clear_str(string):
        new_str = ""
        punctuation_mark = [",", ".", "!", "?", '"', "'", ":", ";", "\n"]
        for i in string:
            if i not in punctuation_mark:
                new_str += i
        return new_str

    def words_command(string):
        the_string = clear_str(string)
        result = 0
        arr = the_string.split(" ")
        for word in arr:
            result += 1
        return result
#проблем с броя думи - изкарва с 1 по малко!? wtf

    def lines_command():
        file = open(sys.argv[1], "r")
        result = 0
        for line in file:
            result += 1
        return result

    def check_command(string):
        if sys.argv[2] == "chars":
            final_result = chars_command(string)
        elif sys.argv[2] == "words":
            final_result = words_command(string)
        else:
            final_result = lines_command()
        return final_result

    the_content = read_file(1)
    print(check_command(the_content))


if __name__ == '__main__':
    main()
