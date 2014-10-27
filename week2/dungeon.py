from orc import Orc
from hero import Hero


class Dungeon:

    entities_dic = {}
    map_array = []
    directions = {"right": 1, "left": -1, "up": -1, "down": 1}

    def __init__(self, path):
        self.path = path
        self.content = self.__path_reading()
        Dungeon.map_array = self.__create_map_array()
        Dungeon.entities_dic = {}

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

    def print_map(self):
        if len(self.map_array) < 0:
            print(self.content)
        else:
            for row in self.map_array:
                print(row)

    def __return_entity_letter(self, entity):
        entity_letter = ""
        if isinstance(entity, Orc):
            entity_letter = "O"
        elif isinstance(entity, Hero):
            entity_letter = "H"
        return entity_letter

    def spawn(self, player_name, entity):
        entity_letter = self.__return_entity_letter(entity)
        for i, row in enumerate(self.map_array):
            for j, sign in enumerate(row):
                if sign == "S":
                    self.map_array[i][j] = entity_letter
                    self.entities_dic[player_name] = [j, i, entity]
                    return
        return False

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

    def __give_me_player_intance(self, player_name):
        tmp_arr = self.entities_dic[player_name]
        entity = tmp_arr[2]
        return entity

    def __move_left_right(self, player_name, direction):
        x, y = self.__give_me_player_own_coordinates(player_name)
        row = self.map_array[y]
        new_x = x + Dungeon.directions[direction]
        if (new_x in range(len(row))) and (self.map_array[y][new_x] == "."):
            self.map_array[y][x] = "."
            entity = self.__give_me_player_intance(player_name)
            entity_letter = self.__return_entity_letter(entity)
            self.map_array[y][new_x] = entity_letter
        else:
            return False

    def __move_up_down(self, player_name, direction):
        x, y = self.__give_me_player_own_coordinates(player_name)
        new_y = y + Dungeon.directions[direction]
        if (new_y in range(len(self.map_array))) and (self.map_array[new_y][x] == "."):
            self.map_array[y][x] = "."
            entity = self.__give_me_player_intance(player_name)
            entity_letter = self.__return_entity_letter(entity)
            self.map_array[new_y][x] = entity_letter
        else:
            return False

    def move(self, player_name, direction):
        if direction == "right" or direction == "left":
            self.__move_left_right(player_name, direction)
            self.__change_player_own_coordinates(player_name, direction)
        elif direction == "up" or direction == "down":
            self.__move_up_down(player_name, direction)
            self.__change_player_own_coordinates(player_name, direction)
        else:
            return False


        # да отида в map_array, да заменя предишната позиция на героя с .
        # да сложа променя позицията на героя спрямо предишната
        # да сложа if conditions кога може да се мести и кога не
