import unittest
from dungeon import Dungeon
from hero import Hero


class DungeonTests(unittest.TestCase):

#test path reading!!!!
    def test_spawn_return_false(self):
        false_map = Dungeon("false_map.txt")
        tmp_content = false_map._path_reading()
        paladin = Hero("Arthas", 100, "Warhammer")
        self.assertFalse(false_map.spawn("player_1", paladin))
        self.assertEqual(false_map._path_reading(), tmp_content)

    def test_spawn_single_location(self):
        file = open("expected_single_location.txt", "r")
        expected_content = file.read()
        file.close()
        single_loc_map = Dungeon("single_map.txt")
        paladin = Hero("Arthas", 100, "Warhammer")
        single_loc_map.spawn("player_1", paladin)
        self.assertEqual(single_loc_map._path_reading(), expected_content)


if __name__ == '__main__':
    unittest.main()


"""
   def test_init(self):
        new_map = Dungeon("false_map.txt")
        self.assertEqual(new_map.c, "false_map.txt")
"""
