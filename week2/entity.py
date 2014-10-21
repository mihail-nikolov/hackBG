class Entity:

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self._maxhealth = health

    def get_health(self):
        return self.health

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def get_damage(self, number):
        self.health -= number
        if self.health < 0:
            self.health = 0

    def take_healing(self, number):
        if self.health == 0:
            return False
        self.health += number
        if self.health > self._maxhealth:
            self.health = self._maxhealth
        return True

