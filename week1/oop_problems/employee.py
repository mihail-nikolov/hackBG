class Employee:

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def get_name(self):
        return "{}, {}".format(self.lname, self.fname)


class HourlyEmployee(Employee):
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname, salary)

    def weekly_pay(self, hours):
        if hours <= 40:
            payment = self.salary*hours
        else:
            overtime_hours = hours - 40
            payment = self.salary*hours + self.salary*overtime_hours*1.5
        return payment

#може ли да се напише 1 фунция за плащане, в която а има if-ове и да се наследява от всички


class SalariedEmployee(Employee):
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname, salary)

    def weekly_pay(self, hours):
        payment = self.salary/52
        return payment


class Manager(Employee):
    def __init__(self, fname, lname, salary, bonus):
        super().__init__(fname, lname, salary)
        self.bonus = bonus

    def weekly_pay(self, hours):
        payment = self.salary/52 + self.bonus
        return payment


goshe = HourlyEmployee("Georgi", "Ivanov", 30)
helena = SalariedEmployee("Elena", "Andonova", 52000)
misho = Manager("Mihail", "Nikolov", 60000, 50)

staff = []
staff.append(goshe)
staff.append(misho)
staff.append(helena)

for employee in staff:
    hours = int(input("Hours worked by " + employee.get_name() + ": "))
    pay = employee.weekly_pay(hours)
    print("Salary: %.2f" % pay)
