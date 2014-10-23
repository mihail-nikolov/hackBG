from orc import Orc
from hero import Hero


class Dungeon:

    def __init__(self, path):
        self.path = path

    def _path_reading(self):
        file = open(self.path, "r")
        content = file.read()
        file.close()
        return content

    def print_map(self):
        print(self._path_reading())

    def spawn(self, player_name, entity):
        content = self._path_reading()
        if "S" not in content:
            return False
        entity_letter = None
        if isinstance(entity, Orc):
            entity_letter = "O"
        elif isinstance(entity, Hero):
            entity_letter = "H"
        else:
            return False
        content = content.replace("S", entity_letter, 1)
        file = open(self.path, "w")
        file.write(content)
        file.close()
