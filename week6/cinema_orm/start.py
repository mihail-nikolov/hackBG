from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from cinema import Cinema

db = 'cinema.db'
Base = declarative_base()
engine = create_engine("sqlite:///cinema.db")
Base.metadata.create_all(engine)
session = Session(bind=engine)

cinema = Cinema(session, db)

cinema.clear_reservation_on_startup()


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


def make_tickets_magic(arr, tickets, proj_id):
    for ticket in range(int(tickets)):
        place = split_command_str(input("Enter <row> <col>"))
        the_place = [int(place[0]), int(place[1])]
        while cinema.is_place_OK(proj_id, the_place) is False:
            print("This seat does not exists or the seat is taken")
            place = split_command_str(input("Enter <row> <col>"))
            the_place = [int(place[0]), int(place[1])]
        arr.append(the_place)
        cinema.write_x(proj_id, the_place)


def print_reserv(movie, seats, date, time):
    message = "This is your reservation:\
    \n Movie: {}\
    \n Date and Time: {} {}\
    \n Seats: {}\
    \n Step 5 (Confirm - type 'finalize') > finalize\
    \n Thanks.".format(movie, date, time, seats)
    print(message)


def main():

    print(start_mess())
    command = split_command_str(input("Type Enter to start>"))
    while command[0] != "give_up":
        command = split_command_str(input("Enter command>"))
        if the_command(command, "show_movies"):
            print_func(cinema.show_movies())

        elif the_command(command, "show_movie_projections"):
            print_func(cinema.show_movie_projection(int(command[1])))

        elif the_command(command, "make_reservation"):
            tickets = input("Enter number of tickets:")
            if tickets == "give_up":
                break
            name = input("Enter name for reservation:")
            if name == "give_up":
                break
            print_func(cinema.show_movies())
            m_id = input("Enter the movie ID:")
            if m_id == "give_up":
                break
            print_func(cinema.show_movie_projection(int(m_id)))
            proj_id = input("Enter projection ID:")
            if proj_id == "give_up":
                break
            theres_no_place = cinema.is_there_place(proj_id, tickets) is False
            while theres_no_place:
                print("There is not enough seats for this projection")
                proj_id = input("Enter projection ID:")
                if proj_id == "give_up":
                    break
            print_hall(cinema.proj_halls[int(proj_id)])
            places_arr = []
            make_tickets_magic(places_arr, tickets, proj_id)
            movie = cinema._get_movie_name(m_id)
            date, time = cinema._get_movie_date_time(proj_id)
            print_reserv(movie, places_arr, date, time)
            confirm = input("Confirm - type 'finalize': ")
            if confirm == "finalize":
                cinema.make_reservation(name, places_arr, proj_id)
            else:
                cinema.del_x(proj_id, places_arr)
                print("You refused your reservation. Bye")

        elif the_command(command, "cancel_reservation"):
            name = input("What is your name: ")
            places_arr = cinema._get_user_places(name)
            proj_id = cinema._get_proj_id_user(name)
            cinema.del_x(proj_id, places_arr)
            cinema.cancel_reservation(name)
            print("your reservation has been deleted")

        elif the_command(command, "exit"):
            print("GoodBye")
            break

        elif the_command(command, "help"):
            print(start_mess())

        else:
            print(unknown_command())


if __name__ == "__main__":
    main()
