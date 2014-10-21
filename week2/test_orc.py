import unittest
import orc


class OrcTests(unittest.TestCase):

    def setUp(self):
        self.orc4o_orc = orc.Orc("Orc4o", 100, 1.5)

    def test_orc_init(self):
        self.assertEqual(self.orc4o_orc.name, "Orc4o")
        self.assertEqual(self.orc4o_orc.health, 100)
        self.assertEqual(self.orc4o_orc.berserk_factor, 1.5)

    def test_set_self_over_berserk_factor(self):
        my_orc = orc.Orc("Orcy", 120, 5)
        self.assertEqual(my_orc.berserk_factor, 2)

    def test_set_self_lower_berserk_factor(self):
        my_orc = orc.Orc("Orcy", 120, 0)
        self.assertEqual(my_orc.berserk_factor, 1)


if __name__ == '__main__':
    unittest.main()
