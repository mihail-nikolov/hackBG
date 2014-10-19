import sys
from random import randint
from time import time
from datetime import datetime

people_dict = {}
files_array = []


def split_command_str(command):
    return tuple(command.split(" "))


def the_command(command_tuple, command):
    return command_tuple[0] == command


def take_money(person, money):
    if person in people_dict:
        people_dict[person] += int(money)
    else:
        people_dict[person] = int(money)
    return people_dict


def current_status(person):
    status_str = ""
    status_str += str(person) + " - " + "0"
    if person in people_dict:
        status_str = str(person) + " - " + str(people_dict[person])
    return status_str


def create_filename():
    ts = time()
    stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
    name = "order" + "_" + str(stamp) + ".txt"
    return name


def create_content(dic):
    cont = ""
    for person in dic:
        cont += str(person) + " - " + str(dic[person]) + "\n"
    return cont

#как да изчистя речника след като съм save-нал поръчката, за да не се преповтаря в следващия файл


def save_command():
    filename = create_filename()
    files_array.append(filename)
    content = create_content(people_dict)
    file = open(filename, 'w+')
    file.write(content)
    file.close()


def list_command(arr):
    for i, el in enumerate(arr):
        print("[{}] {}".format(i+1, el))


def load_command(i, arr):
    if int(i) < 1:
        return "wrong number input"
    else:
        filename = arr[int(i)-1]
        file = open(filename, "r")
        content = file.read()
        return content


def unknown_command():
    message = "Unknown command! \n Try one of the following:\
                \n take <name> <price>\
                \n status \
                \n save \
                \n list \
                \n load <numbers> \
                \n finish \
    "
    return message


def main():
    #count_input_save = 0
    count_input_load = 0
    count_input_finish = 0
    while True:
        command = split_command_str(input("Enter command>"))

        if the_command(command, "take"):
            print(take_money(command[1], command[2]))

        elif the_command(command, "status"):
            print(current_status(command[1]))

        elif the_command(command, "save"):
            save_command()
            #count_input_save += 1

        elif the_command(command, "list"):
            count_input_load += 1
            list_command(files_array)

        elif the_command(command, "load"):
            if count_input_load == 0:
                print("Use list command before loading")
            elif bool(people_dict) is True:
                print("You have not saved the current order.\
                    \n If you wish to discard it, type load <number> again.")
            else:
                print(load_command(command[1], files_array))

        elif the_command(command, "finish"):
            if bool(people_dict) is True and count_input_finish == 0:
                print("You have not saved your order.\
                    \n If you wish to continue, type finish again.\
                    \n If you want to save your order, type save")
                count_input_finish += 1
            else:
                print("Finishing order. Goodbye!")
                break

        else:
            print(unknown_command())


if __name__ == '__main__':
    main()
