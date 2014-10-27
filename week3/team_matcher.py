import requests


start_message = "Hello, you can use one the the following commands:\
                \n list_courses - this lists all the courses that are available now.\
                \n match_teams <course_id>, <team_size>, <group_time> \
             "


def give_me_dict_from_json_api():
    r = requests.get("https://hackbulgaria.com/api/students/", verify=False)
    request_dict = r.json()
    return request_dict


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


def filter_available_people(dic):
    filtered_arr = []
    for element in dic:
        if element["available"] == "true":
            filtered_arr.append(element)
    return filtered_arr


def create_array_of_people_from_given_course(dict, course_id, group_time):

    course_name = return_name_from_course_id(course_id, group_time)



#def match_courses(course_id, team_size, group_time):



def main():
    print(start_message)
    request_dict = give_me_dict_from_json_api()
    while True:
        command = split_command_str(input("Enter command>"))

        if the_command(command, "list_courses"):
            courses_array = list_courses(request_dict)
            print_arr(courses_array)

       # elif the_command(command, "match_teams"):


        else:
            print(unknown_command())


if __name__ == '__main__':
    main()
