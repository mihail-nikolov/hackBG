from movies import Movies
from projections import Projections
from reservation import Reservation

db = "cinema.db"
movies = Movies(db)
projections = Projections(db)
reservation = Reservation(db)


def start_mess():
    start_message = "Hello, here is the cinema. You can \
use one of the the following commands:\
\n show_movies - print all movies ordered by rating\
\n show_movie_projections <movie_id> - \
print all projections of a given movie\
\n make_reservation\
\n cancel_reservation <name> - disintegrate given person's reservation\
\n exit\
\n help"
    return start_message


def print_func(set_obj):
    for row in set_obj:
        print(row)


def print_hall(matrix):
    hall_str = "   1 2 3 4 5 6 7 8 9 10\n"
    for i, row in enumerate(matrix):
        row_num = i + 1
        row_str = str(row_num) + " "
        if row_num != 10:
            row_str += " "
        for col in row:
            row_str += col + " "
        row_str += "\n"
        hall_str += row_str
    print(hall_str)


def split_command_str(command):
    arr = command.split(" ")
    return arr


def the_command(command_arr, command):
    return command_arr[0] == command


def unknown_command():
    message = "Unknown command, you can use one the the following commands:\
                \n show_movies\
                \n show_movie_projections <movie_id> [<date>] \
                \n make_reservation\
                \n cancel_reservation\
                \n exit\
                \n help"
    return message


def print_reserv(name, movie, seats, date, time):
    pass

def main():

    print(start_mess())
    command = split_command_str(input("Type Enter to start>"))
    while command[0] != "give_up":
        command = split_command_str(input("Enter command>"))
        if the_command(command, "show_movies"):
            print_func(movies.show_movies())

        elif the_command(command, "show_movie_projections"):
            print_func(projections.show_movie_projection(int(command[1])))

        elif the_command(command, "make_reservation"):
            tickets = input("Enter number of tickets:")
            if tickets == "give_up":
                break
            name = input("Enter name for reservation:")
            if name == "give_up":
                break
            print_func(movies.show_movies())
            m_id = input("Enter the movie ID:")
            if m_id == "give_up":
                break
            print_func(projections.show_movie_projection(m_id))
            proj_id = input("Enter projection ID:")
            if proj_id == "give_up":
                break
            theres_no_place = projections.is_there_place(proj_id, tickets) is False
            while theres_no_place:
                "There enough seats for this projection"
                proj_id = input("Enter projection ID:")
                if proj_id == "give_up":
                    break
            print_hall(projections.proj_halls[proj_id])
            places_arr = []
            for ticket in range(int(tickets)):
                place = split_command_str(input("Enter <row> <col>"))
                the_place = [int(place[0]), int(place[1])]
                while projections.is_place_OK(the_place) is False:
                    "This seat does not exists or the seat is taken"
                    place = split_command_str(input("Enter <row> <col>"))
                    the_place = [int(place[0]), int(place[1])]
                    if place == "give_up":
                        break
                places_arr.append(the_place)
                projections.write_x(proj_id, the_place)
            confirm = input("Confirm - type 'finalize'")
            if confirm == "finalize":
                reservation.make_reservation(name, places_arr)
            else:
                print("You refused your reservation. Bye")
                break

        elif the_command(command, "cancel_reservation"):
            name = input("What is your name")
            reservation.cancel_reservation(name)

        elif the_command(command, "exit"):
            print("GoodBye")
            break

        elif the_command(command, "help"):
            print(start_mess())

        else:
            print(unknown_command())


if __name__ == "__main__":
    main()
