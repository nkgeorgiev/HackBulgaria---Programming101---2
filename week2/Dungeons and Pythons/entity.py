from weapon import Weapon


class Entity:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.MAX_HEALTH = health
        self.weapon = None

    def get_health(self):
        return self.health

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage_points):
        self.health -= damage_points
        if self.health < 0:
            self.health = 0

    def take_healing(self, healing_points):
        if not self.is_alive():
            return False
        self.health += healing_points
        if self.health > self.MAX_HEALTH:
            self.health = self.MAX_HEALTH
        return True

    def has_weapon(self):
        return self.weapon is not None

    def equip(self, weapon):
        self.weapon = weapon

    def attack(self):
        if not self.has_weapon():
            return 1 #your fists do damage too
        if self.weapon.critical_hit():
            return 2 * self.weapon.damage
        return self.weapon.damage
