import unittest

from cashdesk import Cashdesk

class CashDeskTest(unittest.TestCase):

    def test_total_zero_when_new_instance_made(self):
        my_cashdesk = Cashdesk()
        self.assertEqual(0, my_cashdesk.total())

    def test_total_after_money_take(self):
        my_cashdesk = Cashdesk()
        my_cashdesk.take_money({100: 3, 2: 1})
        self.assertEqual(302, my_cashdesk.total())

    def test_can_withdraw_money_all_money(self):
        my_cashdesk = Cashdesk()
        my_cashdesk.take_money({1: 2, 100: 3})
        self.assertTrue(my_cashdesk.can_withdraw_money(302))

    def test_can_withdraw_money_not_cant_withdraw(self):
        my_cashdesk = Cashdesk()
        my_cashdesk.take_money({1: 2, 100: 3})
        self.assertTrue(my_cashdesk.can_withdraw_money(301))

    def test_can_withdraw_money_cant_withdraw(self):
        my_cashdesk = Cashdesk()
        my_cashdesk.take_money({1: 2, 100: 3})
        self.assertTrue(my_cashdesk.can_withdraw_money(301))

if __name__ == '__main__':
    unittest.main()