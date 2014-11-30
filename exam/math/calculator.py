import random
from operator import add, sub, mul, floordiv


class Calculator():

    def __init__(self):
        self.ops = {"+": add, '-': sub, '*': mul, "//": floordiv, '**': pow}

    def _get_sign(self):
        ops_arr = ["+", "-", '//', '*', '**']
        str_op = random.choice(ops_arr)
        op = self.ops[str_op]
        return str_op, op

    def _get_num(self):
        return random.randint(1, 10)

    def make_str(self, op, num1, num2):
        exp = ''
        exp += str(num1) + str(op) + str(num2)
        return exp

    def make_exp(self):
        str_op, op = self._get_sign()
        num1 = self._get_num()
        num2 = self._get_num()
        return str_op, op, num1, num2

    def calc_result(self, op, num1, num2):
        return op(num1, num2)

    def check_answer(self, ans, res):
        return ans == res
