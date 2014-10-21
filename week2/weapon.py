import random


class Weapon:

    def __init__(self, w_type, damage, critical_strike_percent):
        self.w_type = w_type
        self.damage = damage
        self.return_critical_strike_percent(critical_strike_percent)

    def return_critical_strike_percent(self, critical_strike_percent):
        self.critical_strike_percent = critical_strike_percent
        if self.critical_strike_percent > 1:
            self.critical_strike_percent = 1
        elif self.critical_strike_percent < 0:
            self.critical_strike_percent = 0

    def critical_hit(self):
        if self.critical_strike_percent < random.random():
            return False
        return True
