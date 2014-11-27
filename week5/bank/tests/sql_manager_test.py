import sys
import unittest

sys.path.append("..")

import sql_manager


class SqlManagerTests(unittest.TestCase):

    def setUp(self):
        sql_manager.create_clients_table()
        sql_manager.register('Tester', '123', 'mihail.y.nikolov@abv.bg')

    def tearDown(self):
        sql_manager.cursor.execute('DROP TABLE clients')

    def test_register(self):
        sql_manager.register('Dinko', '123123', "m.nikolov@abv.bg")
        sql_manager.cursor.execute('''SELECT Count(*)  FROM clients
                                    WHERE username = (?)
                                    AND password = (?)''', ('Dinko', '123123'))
        users_count = sql_manager.cursor.fetchone()
        self.assertEqual(users_count[0], 1)

    def test_login(self):
        logged_user = sql_manager.login('Tester')
        self.assertTrue(logged_user.get_username(), 'Tester')

    def test_change_message(self):
        logged_user = sql_manager.login('Tester')
        new_message = "podaivinototam"
        sql_manager.change_message(new_message, logged_user)
        self.assertEqual(logged_user.get_message(), new_message)

    def test_change_password(self):
        logged_user = sql_manager.login('Tester')
        new_password = "12345"
        sql_manager.change_pass(new_password, logged_user)

        logged_user_new_password = sql_manager.login('Tester')
        self.assertEqual(logged_user_new_password.get_username(), 'Tester')

    def test_sql_injection(self):
        logged_user = sql_manager.login("' OR 1 = 1 --")
        self.assertFalse(logged_user)

    def test_get_ran_str(self):
        string = sql_manager.get_ran_str()
        self.assertEqual(len(string), 32)

    def test_check_password(self):
        self.assertFalse(sql_manager.check_password(123, "123"))
        self.assertFalse(sql_manager.check_password(123, 345))
        self.assertTrue(sql_manager.check_password(123, 123))
        self.assertTrue(sql_manager.check_password("misho", "misho"))


if __name__ == '__main__':
    unittest.main()
