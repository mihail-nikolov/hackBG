import unittest
import hero


class HeroTests(unittest.TestCase):

    def setUp(self):
        self.bron_hero = hero.Hero("Bron", 100, "DragonSlayer")

    def test_hero_init(self):
        self.assertEqual(self.bron_hero.name, "Bron")
        self.assertEqual(self.bron_hero.health, 100)
        self.assertEqual(self.bron_hero.nickname, "DragonSlayer")

    def test_hero_known_as(self):
        self.assertEqual(self.bron_hero.hero_known_as(),"Bron the DragonSlayer")


if __name__ == '__main__':
    unittest.main()
