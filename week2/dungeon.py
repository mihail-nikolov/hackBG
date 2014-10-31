from orc import Orc
from hero import Hero
import random
from weapon import Weapon
from fight import Fight


class Dungeon:

    entities_dic = {}
    map_array = []
    directions = {"right": 1, "left": -1, "up": -1, "down": 1}
    weapons = {}

    def __init__(self, path):
        self.path = path
        self.content = self.__path_reading()
        Dungeon.map_array = self.__create_map_array()
        Dungeon.entities_dic = {}
        Dungeon.weapons = {}

    def print_map(self):
        if len(self.map_array) < 0:
            print(self.content)
        else:
            for row in self.map_array:
                print(row)
        for weapon in self.weapons:
            print("{} {} {}".format(weapon.w_type, weapon.damage, weapon.critical_strike_percent))

    def spawn(self, player_name, entity):
        entity_letter = self.__return_entity_letter(entity)
        for i, row in enumerate(self.map_array):
            for j, sign in enumerate(row):
                if sign == "S":
                    self.map_array[i][j] = entity_letter
                    self.entities_dic[player_name] = [j, i, entity]
                    return

    def move(self, player_name, direction):
        if direction == "right" or direction == "left":
            self.__move_left_right(player_name, direction)
            self.__change_player_own_coordinates(player_name, direction)
            self._make_some_actions(player_name)
        elif direction == "up" or direction == "down":
            self.__move_up_down(player_name, direction)
            self.__change_player_own_coordinates(player_name, direction)
            self._make_some_actions(player_name)

    def spawn_weapon(self, weapon):
        x, y = self.__give_me_random_coordinates(self.map_array)
        if self.map_array[y][x] == ".":
            self.map_array[y][x] = "W"
            self.weapons[weapon] = [x, y]
            self.print_map()
        elif self.map_array[y][x] == "#" or self.map_array[y][x] == "W":
            self.spawn_weapon(weapon)
        elif self.map_array[y][x] == "H" or self.map_array[y][x] == "O":
            for player in self.entities_dic:
                pl_x, pl_y = self.__give_me_player_own_coordinates(player)
                if pl_x == x and pl_y == y:
                    pl_inst = self.__give_me_player_intance(player)
                    pl_inst.equip_weapon(weapon)
                    print("{} equipped {}".format(pl_inst.name, weapon.w_type))
                    self.weapons[weapon] = [None, None]

#spawn_weapon is started more than neccessary and when
#I want to delete weapon from self.weapons it throws an error
#I have no problem to delete a weapon from weapons, only in the function up there!!!

    def start_fight(self, player1, player2):
        print("Characters are fighting...")
        pl1_inst = self.__give_me_player_intance(player1)
        pl2_inst = self.__give_me_player_intance(player2)
        fight = Fight(pl1_inst, pl2_inst)
        fight.simulate_fight()
        if pl1_inst.is_alive() is True and pl2_inst.is_alive() is True:
            print("Players don`t have weapons!")
            return
        elif pl1_inst.is_alive() is True:
            winner = player1
            loser = player2
        else:
            winner = player2
            loser = player1
        print("The winner is {}".format(winner))
        self._make_changes_after_fight(winner, loser)

    def __return_entity_letter(self, entity):
        entity_letter = ""
        if isinstance(entity, Orc):
            entity_letter = "O"
        elif isinstance(entity, Hero):
            entity_letter = "H"
        return entity_letter

    def __path_reading(self):
        file = open(self.path, "r")
        content = file.read()
        file.close()
        return content

    def __create_map_array(self):
        map_arr = []
        content = self.__path_reading()
        pieces_arr = content.split("\n")
        for el in pieces_arr:
            tmp_arr = []
            tmp_arr = list(el)
            if len(tmp_arr) > 0:
                map_arr.append(tmp_arr)
        return map_arr

    def __change_player_own_coordinates(self, player_name, direction):
        current_array = self.entities_dic[player_name]
        if direction == "left" or direction == "right":
            current_array[0] += Dungeon.directions[direction]
        elif direction == "up" or direction == "down":
            current_array[1] += Dungeon.directions[direction]

    def __give_me_player_own_coordinates(self, player_name):
        current_array = self.entities_dic[player_name]
        x = current_array[0]
        y = current_array[1]
        return x, y

    def _give_me_weapon_coordinates(self, weapon):
        current_array = self.weapons[weapon]
        x = current_array[0]
        y = current_array[1]
        return x, y

    def __give_me_player_intance(self, player_name):
        tmp_arr = self.entities_dic[player_name]
        entity = tmp_arr[2]
        return entity

    def __move_left_right(self, player_name, direction):
        x, y = self.__give_me_player_own_coordinates(player_name)
        row = self.map_array[y]
        new_x = x + Dungeon.directions[direction]
        if (new_x in range(len(row))) and (self.map_array[y][new_x] != "#"):
            self.map_array[y][x] = "."
            entity = self.__give_me_player_intance(player_name)
            entity_letter = self.__return_entity_letter(entity)
            self.map_array[y][new_x] = entity_letter
        else:
            return False

    def __move_up_down(self, player_name, direction):
        x, y = self.__give_me_player_own_coordinates(player_name)
        new_y = y + Dungeon.directions[direction]
        if (new_y in range(len(self.map_array))) and (self.map_array[new_y][x] != "#"):
            self.map_array[y][x] = "."
            entity = self.__give_me_player_intance(player_name)
            entity_letter = self.__return_entity_letter(entity)
            self.map_array[new_y][x] = entity_letter
        else:
            return False

    def _check_for_equal_player_coordinates(self, player_name):
        cur_x, cur_y = self.__give_me_player_own_coordinates(player_name)
        for player in self.entities_dic:
            if player != player_name:
                pl_x, pl_y = self.__give_me_player_own_coordinates(player)
                if pl_x == cur_x and pl_y == cur_y:
                    return player
        return False

    def _check_for_equal_weapon_coordinates(self, player_name):
        cur_x, cur_y = self.__give_me_player_own_coordinates(player_name)
        for weapon in self.weapons:
            weapon_x, weapon_y = self._give_me_weapon_coordinates(weapon)
            if weapon_x == cur_x and weapon_y == cur_y:
                return weapon
        return False

    def _make_some_actions(self, player_name):
        if self._check_for_equal_weapon_coordinates(player_name) is not False:
            weapon = self._check_for_equal_weapon_coordinates(player_name)
            player_instance = self.__give_me_player_intance(player_name)
            player_instance.equip_weapon(weapon)
            print("{} equipped {}".format(player_instance.name, weapon.w_type))
            del self.weapons[weapon]
        elif self._check_for_equal_player_coordinates(player_name) is not False:
            player_enemy = self._check_for_equal_player_coordinates(player_name)
            self.start_fight(player_name, player_enemy)

#the _check_for_equal_player_coordinates is working
#the problem is only up there!!!!!!

    def __give_me_random_coordinates(self, matrix):
        y = random.randrange(0, len(matrix))
        row = matrix[0]
        x = random.randrange(0, len(row))
        return x, y

    def _make_changes_after_fight(self, winner, loser):
        del self.entities_dic[loser]
        x, y = self.__give_me_player_own_coordinates(winner)
        winner_entity = self.__give_me_player_intance(winner)
        letter = self.__return_entity_letter(winner_entity)
        self.map_array[y][x] = letter

the_map = Dungeon("single_map.txt")
paladin = Hero("Arthas", 100, "Warhammer")
blademaster = Orc("Yurnero", 120, 1.2)
the_map.print_map()
print("----------------")
axe = Weapon("axe", 10, 0.5)
sword = Weapon("sword", 10, 0.8)
the_map.spawn("player_1", paladin)
the_map.spawn("player_2", blademaster)
paladin.equip_weapon(axe)
blademaster.equip_weapon(sword)
the_map.spawn_weapon(axe)
the_map.spawn_weapon(sword)
the_map.print_map()
the_map.move("player_1", "right")
the_map.move("player_2", "down")
the_map.print_map()

print("----------------")
the_map.move("player_1", "down")
the_map.move("player_2", "left")
the_map.print_map()
print("----------------")
the_map.move("player_1", "down")
the_map.move("player_2", "left")
the_map.print_map()
print("----------------")
the_map.move("player_1", "down")
the_map.move("player_2", "left")
the_map.print_map()
print("----------------")

the_map.move("player_2", "left")
the_map.print_map()
print("----------------")
