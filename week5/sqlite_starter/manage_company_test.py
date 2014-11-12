import unittest
from manage_company import monthly_spending, yearly_spending
#from manage_company import add_employee, delete_employee
#import sqlite3


class Manage_company_test(unittest.TestCase):

    def test_monthly_spending(self):
        result = monthly_spending()
        self.assertEqual(result, 26500)

    def test_yearly_spending(self):
        result = yearly_spending()
        self.assertEqual(result, 318000)


if __name__ == '__main__':
    unittest.main()


    #def test_add_employee(self):
        #conn = sqlite3.connect("company.db")
        #cursor = conn.cursor()
        #result = cursor.execute("""SELECT * FROM users""").fetchall()
        #self.assertEqual(len(result), 5)
        #add_employee("Goergie Georgiev", 200, 30, "Software Developer")
        #result = cursor.execute("""SELECT * FROM users""").fetchall()
        #last_one = result[5]
        #the_name = last_one[2]
        #self.assertEqual(len(result), 6)
        #self.assertEqual(the_name, "Goergie Georgiev")
