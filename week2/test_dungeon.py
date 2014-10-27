import unittest
from dungeon import Dungeon
from hero import Hero


class DungeonTests(unittest.TestCase):

    def test_dungeon_init(self):
        new_dungeon = Dungeon("new_dungeon.txt")
        self.assertEqual(new_dungeon.path, "new_dungeon.txt")

    def test_path_reading(self):
        expected_content = "S.##......\n#.##..###.\n#.###.###.\n#.....###.\n###.#####S\n"
        new_dungeon = Dungeon("new_dungeon.txt")
        self.assertEqual(new_dungeon.content, expected_content)

    def test_create_map_array(self):
        new_dungeon = Dungeon("dung_arr.txt")
        expected_array = [["1", "2", "3"], ["4", "5", "6"]]
        self.assertEqual(new_dungeon.map_array, expected_array)

    def test_spawn_return_false(self):
        false_map = Dungeon("false_map.txt")
        tmp_arr = false_map.map_array
        paladin = Hero("Arthas", 100, "Warhammer")
        self.assertFalse(false_map.spawn("player_1", paladin))
        self.assertEqual(false_map.map_array, tmp_arr)

    def test_spawn_single_location(self):
        expected_arr = [['H', '.', '#', '#', '.', '.', '.', '.', '.', '.'],
                        ['#', '.', '#', '#', '.', '.', '#', '#', '#', '.'],
                        ['#', '.', '#', '#', '#', 'S', '#', '#', '#', '.'],
                        ['#', '.', '.', '.', '.', '.', '#', '#', '#', '.'],
                        ['#', '#', '#', '.', '#', '#', '#', '#', '#', '#']]
        single_loc_map = Dungeon("single_map.txt")
        paladin = Hero("Arthas", 100, "Warhammer")
        single_loc_map.spawn("player_1", paladin)
        self.assertEqual(single_loc_map.map_array, expected_arr)

    def test_moving_right_true(self):
        expected_arr = [['.', 'H', '#', '#', '.', '.', '.', '.', '.', '.'],
                        ['#', '.', '#', '#', '.', '.', '#', '#', '#', '.'],
                        ['#', '.', '#', '#', '#', 'S', '#', '#', '#', '.'],
                        ['#', '.', '.', '.', '.', '.', '#', '#', '#', '.'],
                        ['#', '#', '#', '.', '#', '#', '#', '#', '#', '#']]
        single_loc_map = Dungeon("single_map.txt")
        paladin = Hero("Arthas", 100, "Warhammer")
        single_loc_map.spawn("player_1", paladin)
        single_loc_map.move("player_1", "right")
        self.assertEqual(single_loc_map.map_array, expected_arr)

    def test_moving_down_true(self):
        expected_arr = [['.', '.', '#', '#', '.', '.', '.', '.', '.', '.'],
                        ['#', 'H', '#', '#', '.', '.', '#', '#', '#', '.'],
                        ['#', '.', '#', '#', '#', 'S', '#', '#', '#', '.'],
                        ['#', '.', '.', '.', '.', '.', '#', '#', '#', '.'],
                        ['#', '#', '#', '.', '#', '#', '#', '#', '#', '#']]
        single_loc_map = Dungeon("single_map.txt")
        paladin = Hero("Arthas", 100, "Warhammer")
        single_loc_map.spawn("player_1", paladin)
        single_loc_map.move("player_1", "right")
        single_loc_map.move("player_1", "down")
        self.assertEqual(single_loc_map.map_array, expected_arr)

    def test_moving_left_False(self):
        single_loc_map = Dungeon("single_map.txt")
        paladin = Hero("Arthas", 100, "Warhammer")
        single_loc_map.spawn("player_1", paladin)
        self.assertFalse(single_loc_map.move("player_1", "left"))

    def test_moving_up_False(self):
        single_loc_map = Dungeon("single_map.txt")
        paladin = Hero("Arthas", 100, "Warhammer")
        single_loc_map.spawn("player_1", paladin)
        self.assertFalse(single_loc_map.move("player_1", "up"))

    def test_moving_wrong_input(self):
        single_loc_map = Dungeon("single_map.txt")
        paladin = Hero("Arthas", 100, "Warhammer")
        single_loc_map.spawn("player_1", paladin)
        self.assertFalse(single_loc_map.move("player_1", "dqsno"))

if __name__ == '__main__':
    unittest.main()

#как да тестваам private функция?!!?
"""
    def test_give_me_player_own_coordinates(self):
        single_loc_map = Dungeon("single_map.txt")
        paladin = Hero("Arthas", 100, "Warhammer")
        single_loc_map.spawn("player_1", paladin)
        x, y = single_loc_map.__give_me_player_own_coordinates("player_1")
        self.assertEqual(x, 0)
        self.assertEqual(y, 0)
"""
