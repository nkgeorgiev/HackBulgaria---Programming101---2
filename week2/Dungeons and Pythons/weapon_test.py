from weapon import Weapon
import unittest


class TestWeapon(unittest.TestCase):
    def setUp(self):
        self.wep = Weapon("Polearm", 30, 0.5)

    def test_weapon_init(self):
        self.assertEqual(self.wep.type, "Polearm")
        self.assertEqual(self.wep.damage, 30)
        self.assertEqual(self.wep.critical_strike_percent, 0.5)

    def test_critical_hit(self):
        crit = False
        not_crit = False
        n = 1000
        for i in range(n):
            if self.wep.critical_hit():
                crit = True
            else:
                not_crit = True
        self.assertTrue(crit and not_crit)


if __name__ == '__main__':
    unittest.main()
