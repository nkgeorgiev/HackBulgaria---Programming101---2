import random


class Fight:
    def __init__(self, hero, orc):
        self.hero = hero
        self.orc = orc

    def simulate_fight(self):
        coin = round(random.random())
        if coin == 1:
            first = self.hero
            second = self.orc
        else:
            first = self.orc
            second = self.hero

        while first.is_alive() and second.is_alive():
            second.take_damage(first.attack())
            first.take_damage(second.attack())

        if self.hero.is_alive():
            print(self.hero.name + " has won")
            return True
        else:
            print(self.orc.name + " has won")
            return False



