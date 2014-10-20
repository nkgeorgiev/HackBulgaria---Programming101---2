from orc import Orc
from weapon import Weapon
import unittest


class TestOrc(unittest.TestCase):
    def setUp(self):
        self.grom_orc = Orc("Grom", 100, 1.5)

    def test_orc_init(self):
        self.assertEqual("Grom", self.grom_orc.name)
        self.assertEqual(100, self.grom_orc.health)
        self.assertEqual(1.5, self.grom_orc.berserk_factor)

    def test_orc_berserk_factor_init(self):
        self.orc = Orc("Orc", 100, 0.2)
        self.assertEqual(self.orc.berserk_factor, 1)
        self.orc2 = Orc("test", 100, 2.6)
        self.assertEqual(self.orc2.berserk_factor, 2)

    def test_orc_attack(self):
        weapon = Weapon("Axe", 30, 0.2)
        self.grom_orc.equip(weapon)
        crit = False
        not_crit = False
        for i in range(100):
            if self.grom_orc.attack() == 90:
                crit = True
            elif self.grom_orc.attack() == 45:
                not_crit = True
        self.assertTrue(crit and not_crit)


if __name__ == '__main__':
    unittest.main()
