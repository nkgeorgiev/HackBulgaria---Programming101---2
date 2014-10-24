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
        self.filename2 = "basic_dungeon2.txt"
        self.string = "..##.....S\n" \
            "#.##..###.\n" \
            "#.###.###.\n" \
            "#S....###.\n" \
            "###.#####.\n"
        self.string2 = "..##....SS\n" \
            "#.##..###.\n" \
            "#S###.###.\n" \
            "#S....###.\n" \
            "###.#####.\n"
        with open(self.filename, 'w+') as file:
            file.write(self.string)
        with open(self.filename2, "w+") as file:
            file.write(self.string2)
        self.dung = Dungeon(self.filename)
        self.dung2 = Dungeon(self.filename2)
        self.l = self.string2.split('\n')
        self.l.pop()
        self.list = []
        for line in self.l:
            self.list.append(list(line))

        self.test_orc = Orc("Garosh", 100, 1)
        self.test_hero = Hero("Varyan", 100, "test")
        self.spawn_orc = self.dung.spawn("player2", self.test_orc)
        self.spawn_hero = self.dung.spawn("player1", self.test_hero)
        self.spawn_orc2 = self.dung.spawn("player3", self.test_orc)
        #self.dung.print_map()

    def tearDown(self):
        os.remove(self.filename)
        os.remove(self.filename2)

    def test_dungeon_init(self):
        self.assertEqual(self.list, self.dung2.map)

    def test_spawn(self):
        self.assertTrue(self.spawn_hero)
        self.assertTrue(self.spawn_orc)
        self.assertFalse(self.spawn_orc2)

    def test_spawn_right_positions(self):
        player1 = self.dung.players["player2"]
        self.assertListEqual(player1, [self.test_orc, 0, 9])
        self.assertEqual(self.dung.map[0][9], "O")
        self.assertEqual(self.dung.map[3][1], "H")

    def test_move_right(self):
        move_hero_right = self.dung.move("player1", "right")
        move_orc_right = self.dung.move("player2", "right")
        self.assertTrue(move_hero_right)
        self.assertFalse(move_orc_right)

    def test_move_left(self):
        move_hero_left = self.dung.move("player1", "left")
        move_orc_left = self.dung.move("player2", "left")
        self.assertFalse(move_hero_left)
        self.assertTrue(move_orc_left)
        #self.dung.print_map()

    def test_move_up(self):
        move_hero_up = self.dung.move("player1", "up")
        move_orc_up = self.dung.move("player2", "up")
        self.assertTrue(move_hero_up)
        self.assertFalse(move_orc_up)
        #self.dung.print_map()

    def test_move_down(self):
        self.dung.move("player1", "right")
        move_hero_down = self.dung.move("player1", "down")
        move_orc_down = self.dung.move("player2", "down")

        self.assertFalse(move_hero_down)
        self.assertTrue(move_orc_down)
        #self.dung.print_map()

    def test_get_player_by_coordinates(self):
        player = self.dung.get_player_by_coordinates(3, 1)
        self.assertEqual("player1", player)

    def test_fight_right(self):
        self.spawn_hero = self.dung2.spawn("player1", self.test_hero)
        self.spawn_orc = self.dung2.spawn("player2", self.test_orc)
        move_orc_right = self.dung2.move("player1", "right")
        self.assertTrue(move_orc_right)

    def test_fight_left(self):
        self.spawn_hero = self.dung2.spawn("player1", self.test_hero)
        self.spawn_orc = self.dung2.spawn("player2", self.test_orc)

        move_orc_left = self.dung2.move("player2", "left")
        self.assertTrue(move_orc_left)


    def test_fight_up(self):
        self.spawn_hero = self.dung2.spawn("player1", self.test_hero)
        self.spawn_orc = self.dung2.spawn("player2", self.test_orc)
        self.spawn_hero = self.dung2.spawn("player3", self.test_hero)
        self.spawn_orc = self.dung2.spawn("player4", self.test_orc)

        move_orc_up = self.dung2.move("player4", "up")
        self.assertTrue(move_orc_up)

    def test_fight_down(self):
        self.spawn_hero = self.dung2.spawn("player1", self.test_hero)
        self.spawn_orc = self.dung2.spawn("player2", self.test_orc)
        self.spawn_hero = self.dung2.spawn("player3", self.test_hero)
        self.spawn_orc = self.dung2.spawn("player4", self.test_orc)

        move_orc_down = self.dung2.move("player3", "down")
        self.assertTrue(move_orc_down)

if __name__ == '__main__':
    unittest.main()
