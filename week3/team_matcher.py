import requests
import random


start_message = "Hello, you can use one the the following commands:\
                \n list_courses - this lists all the courses that are available now.\
                \n match_teams <course_id>, <team_size>, <group_time> \
             "


def give_me_arr_from_json_api():
    r = requests.get("https://hackbulgaria.com/api/students/", verify=False)
    request_arr = r.json()
    return request_arr


request_arr = give_me_arr_from_json_api()


def split_command_str(command):
    arr = command.split(" ")
    return arr


def the_command(command_tuple, command):
    return command_tuple[0] == command


def list_courses(js_dic):
    courses_arr = []
    for personal_information in js_dic:
        tmp_arr = []
        tmp_arr = personal_information["courses"]
        for element in tmp_arr:
            if element["name"] not in courses_arr:
                courses_arr.append(element["name"])
    return courses_arr

courses_array = list_courses(request_arr)


def print_arr(arr):
    for i, el in enumerate(arr):
        print(("[{}] " " {}\n").format((i + 1), el))


def unknown_command():
    message = "Unknown command, you can use one the the following commands:\
                \n list_courses - this lists all the courses that are available now.\
                \n match_teams <course_id>, <team_size>, <group_time> \
             "
    return message


def return_name_from_course_id(course_id, array):
    if course_id < 1:
        return False
    for index, element in enumerate(array):
        if index + 1 == course_id:
            return element


def filter_available_people():
    filtered_arr = []
    for element in request_arr:
        if element["available"] is True:
            filtered_arr.append(element)
    return filtered_arr


def filter_id_group_time(course_id, group_time):
    group_name = return_name_from_course_id(course_id, courses_array)
    arr = filter_available_people()
    new_arr = []
    for personal_information in arr:
        tmp_arr = []
        tmp_arr = personal_information["courses"]
        for course in tmp_arr:
            if course["name"] == group_name and course["group"] == group_time:
                new_arr.append(personal_information)
    return new_arr


def create_array_of_people_after_filtering(arr):
    new_arr = []
    for personal_information in arr:
        new_arr.append(personal_information["name"])
    return new_arr


def print_groups(arr, team_size):
    random.shuffle(arr)
    counter = 0
    for person in arr:
        if counter == team_size:
            print("-----------")
            counter = 0
        else:
            print(person)
            counter += 1


def match_teams(course_id, team_size, group_time):
    arr = filter_id_group_time(course_id, group_time)
    people_arr = create_array_of_people_after_filtering(arr)
    print_groups(people_arr, team_size)


def main():
    print(start_message)

    while True:
        command = split_command_str(input("Enter command>"))
        if the_command(command, "list_courses"):
            print_arr(courses_array)
        elif the_command(command, "match_teams"):
            match_teams(int(command[1]), int(command[2]), int(command[3]))
        elif the_command(command, "finish"):
            break
        else:
            print(unknown_command())

if __name__ == '__main__':
    main()
