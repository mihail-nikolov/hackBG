class Entity:

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self._maxhealth = health
        self.weapon = None

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

    def equip_weapon(self, weapon):
        self.weapon = weapon
       #print("Weapon Equipped")

    def has_weapon(self):
        if self.weapon is not None:
            return True
        return False

    def attack(self):
        if self.weapon is None:
            return 0
        if self.weapon.critical_hit() is True:
            damage_making = self.weapon.damage*2
        damage_making = self.weapon.damage
        return damage_making
