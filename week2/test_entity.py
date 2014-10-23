import unittest
import entity
from weapon import Weapon


class EntityTests(unittest.TestCase):

    def setUp(self):
        self.entity_hero = entity.Entity("Ivan", 100)

    def test_hero_init(self):
        self.assertEqual(self.entity_hero.name, "Ivan")
        self.assertEqual(self.entity_hero.health, 100)

    def test_get_health(self):
        self.assertEqual(self.entity_hero.get_health(), 100)

    def test_is_alive(self):
        self.assertTrue(self.entity_hero.is_alive())
        self.entity_hero.health = 0
        self.assertFalse(self.entity_hero.is_alive())

    def test_get_damage_int(self):
        self.entity_hero.get_damage(60)
        self.assertEqual(self.entity_hero.health, 40)

    def test_get_damage_float(self):
        self.entity_hero.get_damage(9.5)
        self.assertEqual(self.entity_hero.health, 90.5)

    def test_get_damage_lower_than_0(self):
        self.entity_hero.get_damage(120)
        self.assertEqual(self.entity_hero.health, 0)

    def test_take_healing_death_hero(self):
        self.entity_hero.health = 0
        self.assertFalse(self.entity_hero.take_healing(50))

    def test_take_healing_bigger_than_100(self):
        self.assertTrue(self.entity_hero.take_healing(50))
        self.assertEqual(self.entity_hero.health, self.entity_hero._maxhealth)

    def test_take_healing_normal_healing(self):
        self.entity_hero.health = 50
        self.assertTrue(self.entity_hero.take_healing(40))
        self.assertEqual(self.entity_hero.health, 90)

    def test_equip_weapon(self):
        axe_weapon = Weapon("axe", 20, 0.5)
        self.entity_hero.equip_weapon(axe_weapon)
        self.assertEqual(self.entity_hero.weapon, axe_weapon)

    def test_discard_weapon(self):
        axe_weapon = Weapon("axe", 20, 0.5)
        pen_weapon = Weapon("pen", 5, 0.1)
        self.entity_hero.equip_weapon(axe_weapon)
        self.entity_hero.equip_weapon(pen_weapon)
        self.assertEqual(self.entity_hero.weapon, pen_weapon)

    def test_has_weapon_true(self):
        axe_weapon = Weapon("axe", 20, 0.5)
        self.entity_hero.weapon = axe_weapon
        self.assertTrue(self.entity_hero.has_weapon())

    def test_has_weapon_false(self):
        self.assertFalse(self.entity_hero.has_weapon())

    def test_attack_0_dam(self):
        self.assertEqual(self.entity_hero.attack(), 0)

    def test_attack_crit_dam(self):
        axe_weapon = Weapon("axe", 20, 0.5)
        self.entity_hero.weapon = axe_weapon
        self.assertIn(self.entity_hero.attack(), [20, 40])

if __name__ == '__main__':
    unittest.main()
