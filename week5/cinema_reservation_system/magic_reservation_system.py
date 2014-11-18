from movies import Movies
from projections import Projections

db = "cinema.db"
movies = Movies(db)
projections = Projections(db)


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


def main():

    print(start_mess())

    while True:
        command = split_command_str(input("Enter command>"))
        if the_command(command, "show_movies"):
            movies.show_movies()

        elif the_command(command, "show_movie_projections"):
            projections.show_movie_projection(int(command[1]))

        elif the_command(command, "exit"):
            print("GoodBye")
            break

        elif the_command(command, "help"):
            start_mess()

        else:
            print(unknown_command())


if __name__ == "__main__":
    main()
