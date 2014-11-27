import sql_manager
import re
import getpass
import hashlib
import datetime
import calendar


block_sec = 300


def hash_password(password):
    return hashlib.sha1(password.encode()).hexdigest()


def is_pass_OK(username, passw):
    long_en = len(passw) >= 8
    not_cont_usern = username not in passw
    has_let_cap_let = re.search(r'[a-z]', passw) and re.search(r'[A-Z]', passw)
    has_digit = re.search(r'\d', passw)
    if long_en and not_cont_usern and has_let_cap_let and has_digit:
        if not re.match(r"[~\!@#\$%\^&\*\(\)_\+{}\":;'\[\]]", passw):
            return True
    return False


def pass_conditions(username):
    password = getpass.getpass('Password:')
    while is_pass_OK(username, password) is False:
        print("----------------------------\
        \nMake sure that your password:\
        \n contains more than 8 symbols\
        \n has letters, capital letters, numbers and special symbol\
        \n Username is not in the password (as a substring)")
        password = getpass.getpass('Password:')
    return password


def can_login(username):
    date = datetime.datetime.now()
    cur_time = calendar.timegm(date.utctimetuple())
    blocked_at = sql_manager.get_user_bl_time(username)
    time_not_passed = cur_time - blocked_at < block_sec
    user_blocked = sql_manager.is_blocked(username) == 'True'
    if user_blocked and time_not_passed:
        return False
    return True


def main_menu():
    failed_log_users = [1]
    fail_log_counter = 0
    wrong_pass_limit = 5
    block_message = "you have 5 wrong password inputs\
                    \n and you`re blocked for 5 minutes"

    print("Welcome to our bank service. You are not logged in.\
          \nPlease register or login")

    while True:
        command = input("$$$>")
        if command == 'register':
            username = input("Enter your username: ")
            password = pass_conditions(username)
            hashed_pass = hash_password(password)
            email = input("Enter your emal: ")
            sql_manager.register(username, hashed_pass, email)

            print("Registration Successfull")

        elif command == 'login':
            username = input("Enter your username: ")
            password = getpass.getpass('Password:')
            input_pass = hash_password(password)

            logged_user = sql_manager.login(username)
            existing_pass = sql_manager.get_user_pass(username)
            is_pass_eq = sql_manager.check_password(input_pass, existing_pass) is True
            if logged_user and is_pass_eq and can_login(username) is True:
                fail_log_counter = 0
                sql_manager.unbclock_user(username)
                logged_menu(logged_user)
                failed_log_users = [1]
            else:
                print("Login failed")
                last_user = failed_log_users[len(failed_log_users) - 1]
                if fail_log_counter >= wrong_pass_limit:
                    print(block_message)
                if username == last_user:
                    fail_log_counter += 1
                    if fail_log_counter == wrong_pass_limit:
                        sql_manager.block_user(username)
                        fail_log_counter = 0
                        print(block_message)
                else:
                    fail_log_counter = 1
                failed_log_users.append(username)

        elif command == 'help':
            print("login - for logging in!")
            print("register - for creating new account!")
            print("exit - for closing program!")

        elif command == 'exit':
            break
        else:
            print("Not a valid command")


def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>")

        if command == 'info':
            print("You are: " + logged_user.get_username())
            print("Your id is: " + str(logged_user.get_id()))
            print("Your balance is:" + str(logged_user.get_balance()) + '$')

        elif command == 'changepass':
            username = logged_user.get_username()
            mess_hash_code = sql_manager.get_hashcode()
            mailed_code = sql_manager.send_mail_user(username, mess_hash_code)
            print("We have just sent you an email with hashcode\
                \n To let you to change your password we have to\
                \n make sure that you are the owner of the email.\
                \n type the hash code here:")
            entered_hash = input("hash code: ")
            if sql_manager.check_password(mailed_code, entered_hash):
                new_pass = pass_conditions(username)
                new_hashed_pass = hash_password(new_pass)
                sql_manager.change_pass(new_hashed_pass, logged_user)
                print("Password changing Successfull")
            else:
                print("Sorry the hash code is wrong. Try again!")
        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            sql_manager.change_message(new_message, logged_user)

        elif command == 'show-message':
            print(logged_user.get_message())

        elif command == "withdraw":
            username = logged_user.get_username()
            money = int(input("type money: "))
            balance = sql_manager.get_balance(username)
            if money > balance:
                print("you do not have enough money")
            else:
                input_TAN = input("type TAN: ")
                if sql_manager.is_TAN_usable(username) is False:
                    print("You have to get new TAN")
                elif sql_manager.is_curr_TAN(username, input_TAN) is False:
                    print("Input a valid TAN")
                else:
                    sql_manager.withdraw_money(username, money)
                    sql_manager.increase_TAN_counter(username)
                    print("You have Successfully withdrawed money")

        elif command == "deposit":
            username = logged_user.get_username()
            money = int(input("type money: "))
            input_TAN = input("type TAN: ")
            if sql_manager.is_TAN_usable(username) is False:
                print("You have to get new TAN")
            elif sql_manager.is_curr_TAN(username, input_TAN) is False:
                print("Input a valid TAN")
            else:
                sql_manager.deposit_money(username, money)
                sql_manager.increase_TAN_counter(username)
                print("You have Successfully deposited money")

        elif command == "get-tan":
            username = logged_user.get_username()
            new_TAN = sql_manager.get_ran_str()

            while sql_manager.is_TAN_used(username, new_TAN) is True:
                new_TAN = sql_manager.get_ran_str()
            sql_manager.make_TAN_changes(username, new_TAN)
            sql_manager.send_mail_user(username, new_TAN)
            print('We have sent you email with your new TAN')

        elif command == 'help':
            print("info - for showing account info")
            print("changepass - for changing passowrd")
            print("change-message - for changing users message")
            print("show-message - for showing users message")
            print("withdraw - withdraw money")
            print("deposit - deposit money")
            print("get-tan - calculating new TAN")


def main():
    sql_manager.create_clients_table()
    main_menu()

if __name__ == '__main__':
    main()
