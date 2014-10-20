from fight import Fight
from hero import Hero
from orc import Orc
from weapon import Weapon
import unittest


class TestFight(unittest.TestCase):
    def setUp(self):
        self.grom_orc = Orc("Grom", 100, 1.2)
        self.bron_hero = Hero("Bron", 100, "DragonSlayer")
        sword = Weapon("sword", 10, 0.4)
        axe = Weapon("Axe", 10, 0.4)
        self.grom_orc.equip(axe)
        self.bron_hero.equip(sword)
        self.fight = Fight(self.bron_hero, self.grom_orc)

    def test_fight_init(self):
        self.assertEqual(self.bron_hero, self.fight.hero)
        self.assertEqual(self.grom_orc, self.fight.orc)

    def test_simulate_fight(self):
        hero_won = False
        orc_won = False
        for i in range(100):
            self.fight.simulate_fight()
            if self.bron_hero.is_alive():
                hero_won = True
            else:
                orc_won = True
            self.bron_hero.health = 100
            self.grom_orc.health = 100
        self.assertTrue(hero_won and orc_won)
if __name__ == '__main__':

    unittest.main()
