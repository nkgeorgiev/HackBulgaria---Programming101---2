import random


class Weapon:
    def __init__(self, type, damage, critical_strike_percent):
        self.type = type
        self.damage = damage
        self._set_critital_strike_percent(critical_strike_percent)

    def _set_critital_strike_percent(self, critical_strike_percent):
        if critical_strike_percent > 1:
            self.critical_strike_percent = 1
        elif critical_strike_percent < 0:
            self.critical_strike_percent = 0
        else:
            self.critical_strike_percent = critical_strike_percent

    def critical_hit(self):
        return random.random() < self.critical_strike_percent

