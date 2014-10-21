class Fraction:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def compare(self):
        if self.number1 == self.number2:
            return "{} == {}".format(self.number1, self.number2)
        elif self.number1 > self.number2:
            return "{} > {}".format(self.number1, self.number2)
        else:
            return "{} < {}".format(self.number1, self.number2)

    def sum_nums(self):
        return self.number1 + self.number2

    def multiply_nums(self):
        return self.number1 - self.number2



a = Fraction(1, 2)
print(a.compare())
print(a.sum_nums())
print(a.multiply_nums())


