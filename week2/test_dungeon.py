import unittest
from dungeon import Dungeon
from hero import Hero
from orc import Orc
from weapon import Weapon


class DungeonTests(unittest.TestCase):

    def setUp(self):
        self.single_loc_map = Dungeon("single_map.txt")
        self.paladin = Hero("Arthas", 100, "Warhammer")
        self.single_loc_map.spawn("player_1", self.paladin)

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
        self.assertFalse(false_map.spawn("player_1", self.paladin))
        self.assertEqual(false_map.map_array, tmp_arr)

    def test_spawn_single_location(self):
        expected_arr = [['H', '.', '#', '#', '.', '.', '.', '.', '.', '.'],
                        ['#', '.', '#', '#', '.', '.', '#', '#', '#', '.'],
                        ['#', '.', '#', '#', '#', 'S', '#', '#', '#', '.'],
                        ['#', '.', '.', '.', '.', '.', '#', '#', '#', '.'],
                        ['#', '#', '#', '.', '#', '#', '#', '#', '#', '#']]
        self.assertEqual(self.single_loc_map.map_array, expected_arr)

    def test_moving_right_true(self):
        expected_arr = [['.', 'H', '#', '#', '.', '.', '.', '.', '.', '.'],
                        ['#', '.', '#', '#', '.', '.', '#', '#', '#', '.'],
                        ['#', '.', '#', '#', '#', 'S', '#', '#', '#', '.'],
                        ['#', '.', '.', '.', '.', '.', '#', '#', '#', '.'],
                        ['#', '#', '#', '.', '#', '#', '#', '#', '#', '#']]
        self.single_loc_map.move("player_1", "right")
        self.assertEqual(self.single_loc_map.map_array, expected_arr)

    def test_moving_down_true(self):
        expected_arr = [['.', '.', '#', '#', '.', '.', '.', '.', '.', '.'],
                        ['#', 'H', '#', '#', '.', '.', '#', '#', '#', '.'],
                        ['#', '.', '#', '#', '#', 'S', '#', '#', '#', '.'],
                        ['#', '.', '.', '.', '.', '.', '#', '#', '#', '.'],
                        ['#', '#', '#', '.', '#', '#', '#', '#', '#', '#']]
        self.single_loc_map.move("player_1", "right")
        self.single_loc_map.move("player_1", "down")
        self.assertEqual(self.single_loc_map.map_array, expected_arr)

    def test_moving_left_False(self):
        self.assertFalse(self.single_loc_map.move("player_1", "left"))

    def test_moving_up_False(self):
        self.assertFalse(self.single_loc_map.move("player_1", "up"))

    def test_moving_wrong_input(self):
        self.assertFalse(self.single_loc_map.move("player_1", "dqsno"))

    def test_give_me_player_own_coordinates(self):
        x, y = self.single_loc_map._give_me_own_players_coordinates("player_1")
        self.assertEqual(x, 0)
        self.assertEqual(y, 0)

    def test_return_entity_letter(self):
        self.assertEqual(self.single_loc_map._return_entity_letter(self.paladin), "H")

    def test_give_me_own_players_coordinates(self):
        x, y = self.single_loc_map._give_me_own_players_coordinates("player_1")
        self.assertEqual(x, 0)
        self.assertEqual(y, 0)

    def test_change_own_players_coordinates_down_right(self):
        self.single_loc_map._change_own_players_coordinates("player_1", "right")
        self.single_loc_map._change_own_players_coordinates("player_1", "down")
        tmp_arr = self.single_loc_map.entities_dic["player_1"]
        x = tmp_arr[0]
        y = tmp_arr[1]
        self.assertEqual(x, 1)
        self.assertEqual(y, 1)

    def test_give_me_player_instance(self):
        instance = self.single_loc_map._give_me_player_instance("player_1")
        self.assertEqual(self.paladin, instance)

    def test_move_left_right(self):
        self.assertFalse(self.single_loc_map._move_left_right("player_1", "left"))
        expected_arr = [['.', 'H', '#', '#', '.', '.', '.', '.', '.', '.'],
                        ['#', '.', '#', '#', '.', '.', '#', '#', '#', '.'],
                        ['#', '.', '#', '#', '#', 'S', '#', '#', '#', '.'],
                        ['#', '.', '.', '.', '.', '.', '#', '#', '#', '.'],
                        ['#', '#', '#', '.', '#', '#', '#', '#', '#', '#']]
        self.single_loc_map._move_left_right("player_1", "right")
        self.assertEqual(self.single_loc_map.map_array, expected_arr)
        tmp_arr = self.single_loc_map.entities_dic["player_1"]
        x = tmp_arr[0]
        y = tmp_arr[1]
        self.assertEqual(x, 1)
        self.assertEqual(y, 0)

    def test_move_up_down(self):
        self.assertFalse(self.single_loc_map._move_up_down("player_1", "down"))
        self.assertFalse(self.single_loc_map._move_up_down("player_1", "up"))
        expected_arr = [['.', '.', '#', '#', '.', '.', '.', '.', '.', '.'],
                        ['#', 'H', '#', '#', '.', '.', '#', '#', '#', '.'],
                        ['#', '.', '#', '#', '#', 'S', '#', '#', '#', '.'],
                        ['#', '.', '.', '.', '.', '.', '#', '#', '#', '.'],
                        ['#', '#', '#', '.', '#', '#', '#', '#', '#', '#']]
        self.single_loc_map._move_left_right("player_1", "right")
        self.single_loc_map._move_up_down("player_1", "down")
        self.assertEqual(self.single_loc_map.map_array, expected_arr)
        tmp_arr = self.single_loc_map.entities_dic["player_1"]
        x = tmp_arr[1]
        y = tmp_arr[1]
        self.assertEqual(x, 1)
        self.assertEqual(y, 1)

    def test_check_for_equal_player_coordinates(self):
        blademaster = Orc("Yurnero", 120, 1.2)
        self.single_loc_map.spawn("player_2", blademaster)
        answer1 = self.single_loc_map._check_for_equal_player_coordinates("player_1")
        self.assertFalse(answer1)
        self.single_loc_map.move("player_1", "right")
        self.single_loc_map.move("player_2", "down")
        self.single_loc_map.move("player_1", "down")
        self.single_loc_map.move("player_2", "left")
        self.single_loc_map.move("player_1", "down")
        self.single_loc_map.move("player_2", "left")
        self.single_loc_map.move("player_1", "down")
        self.single_loc_map.move("player_2", "left")
        self.single_loc_map.move("player_2", "left")
        answer2 = self.single_loc_map._check_for_equal_player_coordinates("player_1")
        answer3 = self.single_loc_map._check_for_equal_player_coordinates("player_2")
        self.assertEqual(answer2, "player_2")
        self.assertEqual(answer3, "player_1")

    def test_give_me_random_coordinates(self):
        matrix = self.single_loc_map.map_array
        a, b = self.single_loc_map._give_me_random_coordinates(matrix)
        self.assertIn(a, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertIn(b, [0, 1, 2, 3, 4])

    def test_check_for_equal_weapon_coordinates_false1(self):
        answer = self.single_loc_map._check_for_equal_player_coordinates("player_1")
        self.assertFalse(answer)

    def test_check_for_equal_weapon_coordinates_false2(self):
        axe = Weapon("axe", 10, 0.5)
        self.paladin.equip_weapon(axe)
        answer = self.single_loc_map._check_for_equal_player_coordinates("player_1")
        self.assertFalse(answer)

    def test_start_fight_both_alive(self):
        fight_map = Dungeon("fight_map.txt")
        blademaster = Orc("Yurnero", 120, 1.2)
        fight_map.spawn("player_1", self.paladin)
        fight_map.spawn("player_2", blademaster)
        fight_map.move("player_1", "right")
        fight_map.move("player_2", "left")
        fight_map.move("player_1", "right")
        self.assertTrue(self.paladin.is_alive())
        self.assertTrue(blademaster.is_alive())

    def test_start_fight_blademaster_dead(self):
        axe = Weapon("axe", 10, 0.5)
        blademaster = Orc("Yurnero", 120, 1.2)
        self.paladin.equip_weapon(axe)
        fight_map = Dungeon("fight_map.txt")
        fight_map.spawn("player_1", self.paladin)
        fight_map.spawn("player_2", blademaster)
        fight_map.move("player_1", "right")
        fight_map.move("player_2", "left")
        fight_map.move("player_1", "right")
        expected_arr = [['.', '.', 'H', '.']]
        self.assertTrue(self.paladin.is_alive())
        self.assertFalse(blademaster.is_alive())
        #testing _make_changes_after_fight
        self.assertEqual(fight_map.map_array, expected_arr)

    def test_start_fight_paladin_dead(self):
        axe = Weapon("axe", 10, 0.5)
        blademaster = Orc("Yurnero", 120, 1.2)
        blademaster.equip_weapon(axe)
        fight_map = Dungeon("fight_map.txt")
        fight_map.spawn("player_1", self.paladin)
        fight_map.spawn("player_2", blademaster)
        fight_map.move("player_1", "right")
        fight_map.move("player_2", "left")
        fight_map.move("player_1", "right")
        expected_arr = [['.', '.', 'O', '.']]
        self.assertFalse(self.paladin.is_alive())
        self.assertTrue(blademaster.is_alive())
        #testing _make_changes_after_fight
        self.assertEqual(fight_map.map_array, expected_arr)


if __name__ == '__main__':
    unittest.main()

#I did not test give_me_weapon_coordinates
#_check_for_equal_weapon_coordinates and make_some_acctions
