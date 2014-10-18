import unittest

from word_count import word_count


class word_count_test(unittest.TestCase):

    def test_expected_number_words(self):
        array = ["apple", "bottle", "apple", "little", "little"]
        dic = word_count(array)
        self.assertEqual(2, dic["apple"])

    def test_array_of_numbers(self):
        array = [1, 2, 2, 2, 3]
        dic = word_count(array)
        self.assertEqual(3, dic[2])

    def test_empty_arr(self):
        array = []
        dic = word_count(array)
        self.assertEqual({}, dic)

if __name__ == '__main__':
    unittest.main()
