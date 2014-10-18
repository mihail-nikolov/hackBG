import unittest

from spam_eggs import prepare_meal, add_eggs, add_spam


class test_spam_eggs(unittest.TestCase):

    def test_add_eggs(self):
        self.assertEqual("eggs", add_eggs(20))

    def test_add_spam(self):
        self.assertEqual("spam ", add_spam(3))

    def test_prepare_meal(self):
        self.assertEqual("spam and eggs", prepare_meal(15))

if __name__ == '__main__':
    unittest.main()
