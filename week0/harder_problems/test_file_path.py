import unittest

from file_path import make_array, reduce_file_path


class test_reduce_file_path(unittest.TestCase):

    def test_make_arr(self):
        string = "/srv/www/htdocs/wtf"
        arr = make_array(string)
        excepted_arr = ["srv", "www", "htdocs", "wtf"]
        self.assertEqual(excepted_arr, make_array(string))

    def test_reduce_file_path(self):
        string = "/srv/www/htdocs/./wtf/blq/.."
        excepted_str = "/srv/www/htdocs/wtf"
        self.assertEqual(excepted_str, reduce_file_path(string))

if __name__ == '__main__':
    unittest.main()
