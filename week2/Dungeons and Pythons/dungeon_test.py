from fight import Fight
from hero import Hero
from orc import Orc
from weapon import Weapon
from dungeon import Dungeon
import unittest
import os


class TestDungeon(unittest.TestCase):
    def setUp(self):
        self.filename = "basic_dungeon.txt"
        self.string = "S.##......\n" \
            "#.##..###.\n" \
            "#.###.###.\n" \
            "#.....###.\n" \
            "###.#####S\n"
        with open(self.filename, 'w+') as file:
            file.write(self.string)

        self.dung = Dungeon(self.filename)
        self.l = self.string.split('\n')
        self.l.pop()
        self.list = []
        for line in self.l:
            self.list.append(list(line))

        self.test_orc = Orc("test_orc", 100, 1.2)
        self.test_hero = Hero("test_hero", 100, "test")


    def tearDown(self):
        pass
        os.remove(self.filename)

    def test_dungeon_init(self):
        self.assertEqual(self.list, self.dung.map)

    def test_spawn(self):
        self.spawn_hero = self.dung.spawn("player1", self.test_hero)
        self.spawn_orc = self.dung.spawn("player2", self.test_orc)
        self.spawn_orc2 = self.dung.spawn("player3", self.test_orc)

        self.assertTrue(self.spawn_hero)
        self.assertTrue(self.spawn_orc)
        self.assertFalse(self.spawn_orc2)
        player1 = self.dung.players["player2"]
        self.assertListEqual(player1, [self.test_orc, 4,9])
        self.assertEqual(self.dung.map[4][9], "O")
        self.assertEqual(self.dung.map[0][0], "H")

    def test_move_left(self):
        self.dung.spawn("player1", self.test_hero)
        self.dung.spawn("player2", self.test_orc)
        move_hero_left = self.dung.move("player1", "left")
        move_orc_left = self.dung.move("player2", "left")
        self.assertTrue(move_hero_left)
        self.assertFalse(move_orc_left)

    def test_move_right(self):
        self.dung.spawn("player1", self.test_hero)
        self.dung.spawn("player2", self.test_orc)
        move_hero_right = self.dung.move("player1", "right")
        move_orc_right = self.dung.move("player2", "right")
        self.assertTrue(move_hero_right)
        self.assertFalse(move_orc_right)

    def test_move_up(self):
        self.dung.spawn("player1", self.test_hero)
        self.dung.spawn("player2", self.test_orc)
        move_hero_up = self.dung.move("player1", "up")
        move_orc_up = self.dung.move("player2", "up")
        self.assertTrue(move_hero_up)
        self.assertFalse(move_orc_up)

    def test_move_down(self):
        self.dung.spawn("player1", self.test_hero)
        self.dung.spawn("player2", self.test_orc)
        move_hero_down = self.dung.move("player1", "down")
        move_orc_down = self.dung.move("player2", "down")
        self.assertTrue(move_hero_down)
        self.assertFalse(move_orc_down)

if __name__ == '__main__':
    unittest.main()
