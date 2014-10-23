import random


class Fight:

    def __init__(self, orc, hero):
        self.orc = orc
        self.hero = hero

    def _set_turn(self):
        turn_coin = random.random()
        if turn_coin <= 0.5:
            attacker = self.orc
            attacked = self.hero
        else:
            attacker = self.hero
            attacked = self.orc
        return attacker, attacked

    def simulate_fight(self):
        attacker, attacked = self._set_turn()
        print("{} health is: {}".format(attacker.name, attacker.health))
        print("{} health is: {}".format(attacked.name, attacked.health))
        while self.orc.is_alive() and self.hero.is_alive():
            damage = attacker.attack()
            attacked.get_damage(damage)
            print("{} health is: {}".format(attacked.name, attacked.health))
            attacked, attacker = attacker, attacked
