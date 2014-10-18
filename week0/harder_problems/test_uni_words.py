import unittest

from uni_words import uni_words


class test_uni_words(unittest.TestCase):

    def test_expected_number_words(self):
        array = ["apple", "bottle", "apple", "little", "little"]
        a = uni_words(array)
        self.assertEqual(3, a)

    def test_array_of_numbers(self):
        array = [1, 2, 2, 2, 3]
        a = uni_words(array)
        self.assertEqual(3, a)

    def test_empty_arr(self):
        array = []
        a = uni_words(array)
        self.assertEqual(0, a)

if __name__ == '__main__':
    unittest.main()
