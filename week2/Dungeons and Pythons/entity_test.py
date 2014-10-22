from entity import Entity
from weapon import Weapon
import unittest


class TestEntity(unittest.TestCase):

    def setUp(self):
        self.test_entity = Entity("test_entity", 100)

    def test_test_entity_init(self):
        self.assertEqual("test_entity", self.test_entity.name)
        self.assertEqual(100, self.test_entity.health)

    def test_get_health(self):
        self.assertEqual(100, self.test_entity.get_health())

    def test_is_alive(self):
        self.assertTrue(self.test_entity.is_alive())

    def test_is_dead(self):
        self.test_entity.health = 0
        self.assertFalse(self.test_entity.is_alive())

    def test_take_damage(self):
        self.test_entity.take_damage(24)
        self.assertEqual(self.test_entity.health, 76)

    def test_take_more_damage(self):
        self.test_entity.take_damage(123)
        self.assertEqual(self.test_entity.health, 0)

    def test_take_healing(self):
        self.test_entity.take_damage(24)
        heal_result = self.test_entity.take_healing(12)
        self.assertEqual(self.test_entity.health, 88)
        self.assertTrue(heal_result)

    def test_take_more_healing(self):
        self.test_entity.take_damage(20)
        heal_result = self.test_entity.take_healing(40)
        self.assertEqual(self.test_entity.health, 100)
        self.assertTrue(heal_result)

    def test_take_healing_when_dead(self):
        self.test_entity.take_damage(123)
        heal_result = self.test_entity.take_healing(12)
        self.assertEqual(self.test_entity.health, 0)
        self.assertFalse(heal_result)

    def test_has_weapon(self):
        self.assertFalse(self.test_entity.has_weapon())
        weapon = Weapon("Axe", 30, 0.2)
        self.test_entity.equip(weapon)
        self.assertTrue(self.test_entity.has_weapon())

    def test_attack_without_weapon(self):
        self.assertEqual(self.test_entity.attack(), 1)

    def test_attack(self):
        weapon = Weapon("Axe", 30, 0.2)
        self.test_entity.equip(weapon)
        crit = False
        not_crit = False
        for i in range(100):
            if self.test_entity.attack() == 60:
                crit = True
            elif self.test_entity.attack() == 30:
                not_crit = True
        self.assertTrue(crit and not_crit)

if __name__ == '__main__':
    unittest.main()
