class cashdesk:

    def __init__(self, money = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}):
        self.money = money

    def take_money(self, money_dict):
        for i in money_dict:
            self.money[i] += money_dict[i]

    def total(self):
        total_sum = 0
        for i in self.money:
            total_sum += i * self.money[i]
        return total_sum

    def can_withdraw_money(self, am_money):
        if self.total() < am_money:
            return False
        else:
            arr = [100, 50, 20, 10, 5, 2, 1]
            for i in arr:
                while self.money[i] != 0:
                    if am_money - i >= 0:
                        am_money -= i
                        self.money[i] -= 1
                    else:
                        break
            if am_money == 0:
                return True
            else:
                return False


my_cashdesk = cashdesk()
my_cashdesk.take_money({100: 1, 50: 2, 2: 1})
print(my_cashdesk.money)
print(my_cashdesk.total())
print(my_cashdesk.can_withdraw_money(152))
