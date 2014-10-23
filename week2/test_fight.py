import unittest
from weapon import Weapon
from orc import Orc
from hero import Hero
from fight import Fight


class FightTests(unittest.TestCase):

    def setUp(self):
        self.orc_goshe = Orc("Georgi", 100, 1.2)
        self.hero_slayer = Hero("DragonSlayer", 100, "Killer")
        self.axe = Weapon("Axe", 10, 0.2)
        self.sword = Weapon("Sword", 12, 0.5)
        self.orc_goshe.weapon = self.axe
        self.hero_slayer.weapon = self.sword
        self.battle_one = Fight(self.orc_goshe, self.hero_slayer)

    def test_fight_init(self):
        self.assertEqual(self.battle_one.orc, self.orc_goshe)
        self.assertEqual(self.battle_one.hero, self.hero_slayer)

#как да тествам кой е attacker???!!!!

    def test_who_is_attacked_and_attacker(self):
        result_array = []
        attacker, attacked = self.battle_one._set_turn()
        result_array.append(attacked)
        result_array.append(attacker)
        self.assertIn(self.orc_goshe, result_array)
        self.assertIn(self.hero_slayer, result_array)

    def test_simulate_battle_fight_without_weapon(self):
        self.orc_goshe.weapon = None
        self.battle_one.simulate_fight()
        self.assertFalse(self.orc_goshe.is_alive())

    def test_simulate_battle_fight(self):
        self.battle_one.simulate_fight()
        result_array = []
        result_array.append(self.orc_goshe.is_alive())
        result_array.append(self.hero_slayer.is_alive())
        self.assertIn(False, result_array)


if __name__ == '__main__':
    unittest.main()
