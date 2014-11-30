from calculator import Calculator
from game import Game
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


db = 'players.db'
Base = declarative_base()
engine = create_engine("sqlite:///players.db")
Base.metadata.create_all(engine)
session = Session(bind=engine)

game = Game(session, db)
calc = Calculator()


def start_mess():
    start_message = "Welcome to the 'Do you even math?' game!\
\n Here are your options:\
\n- start\
\n- highscores"
    return start_message


def print_func(set_obj):
    for row in set_obj:
        print(row)
        #make some corrections to print the right way!


def split_command_str(command):
    arr = command.split(" ")
    return arr


def the_command(command_arr, command):
    return command_arr[0] == command


def unknown_command():
    message = "\n Here are your options:\
\n- start\
\n- highscores"
    return message


def game_over(points):
    message = "Incorrect! Ending game. You score is:{}.format"(points)
    return message


def main():

    print(start_mess())
    while True:
        command = split_command_str(input(">"))
        if the_command(command, "start"):
            name = input('enter your playername: ')
            print('Welcome {}! Let the game begin!'.format(name))
            game.add_user(name, 0, 0)
            while True:
                print('The question is: ')
                str_op, op, num1, num2 = calc.make_exp()
                correct_result = calc.calc_result(op, num1, num2)
                the_exp_str = calc.make_str(str_op, num1, num2)
                the_quest = 'What is the answer to:' + the_exp_str
                print(the_quest)
                answer = int(input(">"))
                if calc.check_answer(answer, correct_result) is True:
                    game._increase_result(name)
                    print("Correct!")
                else:
                    result = game._get_result(name)
                    points = game.calculate_points(name, result)
                    print("Incorrect!")
                    print("your score is: {}".format(points))
                    break

        elif the_command(command, "highscores"):
            print_func(game.get_rating_table())

        elif the_command(command, "exit"):
            print("Bye!")
            break

        else:
            print(unknown_command())


if __name__ == "__main__":
    main()
