import sqlite3

MONTHS_YEAR = 12

conn = sqlite3.connect("company.db")
cursor = conn.cursor()


start_message = "Hello, here is the company. You can \
use one of the the following commands:\
\n list_employees\
\n monthly_spending - Prints out the total sum for monthly \
spending that the company is doing for salaries\
\n yearly_spending - Prints out the total sum \
for one year of operation (Again, salaries)\
\n add_employee - the program starts to promt \
for data, to create a new employee\
\n delete_employee <id> - the program should \
delete the given employee from the database \
\n update_employee <employee_id>, the program should prompt\
the user to change each of the fields for the given employee"


def split_command_str(command):
    arr = command.split(" ")
    return arr


def the_command(command_arr, command):
    return command_arr[0] == command


def unknown_command():
    message = "Unknown command, you can use one the the following commands:\
                \n list_employees\
                \n monthly_spending \
                \n yearly_spending\
                \n add_employee\
                \n delete_employee <id>\
                \n update_employee <employee_id>"
    return message


def list_employees():
    result = cursor.execute("SELECT id, name, position FROM users")
    for row in result:
        print("{}| {} - {}".format(row[0], row[1], row[2]))


def monthly_spending():
    month_salary = 0
    result = cursor.execute("SELECT monthly_salary FROM users")
    for money in result:
        month_salary += int(money[0])
    return month_salary


def calculate_whole_bonus():
    bonus = cursor.execute("SELECT yearly_bonus FROM users")
    result = 0
    for money in bonus:
        result += int(money[0])
    return result


def yearly_spending():
    month_salary = monthly_spending()
    the_bonus = calculate_whole_bonus()
    year_salary = MONTHS_YEAR * month_salary + the_bonus
    return year_salary


def add_employee():
    name, salary, bonus, position = input_info()
    new_employee = (name, salary, bonus, position)
    cursor.execute("""INSERT INTO users(name, monthly_salary, yearly_bonus,
                            position)VALUES(?, ?, ?, ?)""", new_employee)
    conn.commit()


def delete_employee(id):
    cursor.execute("""DELETE FROM users WHERE id = ?""", (id,))
    conn.commit()


def input_info():
    name = input("Employee Name: ")
    salary = input("Monthly Salary: ")
    bonus = input("Yearly Bonus: ")
    position = input("Position: ")
    return name, salary, bonus, position


def update_employee(id):
    name, salary, bonus, position = input_info()
    cursor.execute("UPDATE users SET name = ? WHERE id = ?", (name, id))
    cursor.execute("UPDATE users SET monthly_salary = ? WHERE id = ?", (salary, id))
    cursor.execute("UPDATE users SET yearly_bonus = ? WHERE id = ?", (bonus, id))
    cursor.execute("UPDATE users SET position = ? WHERE id = ?", (position, id))
    conn.commit()


def main():

    print(start_message)

    while True:
        command = split_command_str(input("Enter command>"))
        if the_command(command, "list_employees"):
            list_employees()

        elif the_command(command, "monthly_spending"):
            print(monthly_spending())

        elif the_command(command, "yearly_spending"):
            print(yearly_spending())

        elif the_command(command, "add_employee"):
            add_employee()

        elif the_command(command, "delete_employee"):
            delete_employee(int(command[1]))

        elif the_command(command, "update_employee"):
            update_employee(int(command[1]))

        elif the_command(command, "finish"):
            print("GoodBye")
            break

        else:
            print(unknown_command())


if __name__ == "__main__":
    main()

