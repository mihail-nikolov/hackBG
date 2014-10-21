import unittest
from weapon import Weapon


class WeaponTests(unittest.TestCase):

    def test_weapon_init(self):
        axe = Weapon("axe", 10, 0.5)
        self.assertEqual(axe.w_type, "axe")
        self.assertEqual(axe.damage, 10)
        self.assertEqual(axe.critical_strike_percent, 0.5)

    def test_return_critical_strike_percent_over(self):
        axe = Weapon("axe", 10, 2)
        self.assertEqual(axe.critical_strike_percent, 1)

    def test_return_critical_strike_percent_lower(self):
        axe = Weapon("axe", 10, -3)
        self.assertEqual(axe.critical_strike_percent, 0)

    def test_critical_hit(self):
        weapon = Weapon("axe", 10, 0.5)
        results = []
        for x in range(1000):
            results.append(weapon.critical_hit())
        self.assertTrue(True in results)
        self.assertTrue(False in results)





  #  def test_

if __name__ == '__main__':
    unittest.main()
