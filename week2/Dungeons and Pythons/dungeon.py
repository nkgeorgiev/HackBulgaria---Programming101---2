from hero import Hero
from orc import Orc


class Dungeon:
    def __init__(self, filepath):
        self.map = self.__set_map(filepath)
        self.players = {}
        self.height = len(self.map) - 1
        self.width = len(self.map[0]) - 1

    def __set_map(self, filepath):
        with open(filepath, 'r') as file:
            string = file.read()
            m = string.split('\n')
        m.pop()

        map = []
        for line in m:
            l = list(line)
            map.append(l)
        return map

    def print_map(self):
        for line in self.map:
            print(line)

    def spawn(self, player_name, entity):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == 'S':
                    self.players[player_name] = [entity, i, j]
                    if type(entity) is Orc:
                        self.map[i][j] = 'O'
                    else:
                        self.map[i][j] = 'H'
                    return True
        return False

    def move(self, player_name, direction):
        player = self.players[player_name]
        x = player[1]
        y = player[2]
        if direction == "left":
            if y + 1 < self.width and self.map[x][y+1] == ".":
                y += 1
                return True

        elif direction == "right":
            if y - 1 >= 0 and self.map[x][y-1] == ".":

                y -= 1
                return True

        elif direction == "up":
            if x - 1 >= 0 and self.map[x-1][y] == ".":
                x -= 1
                return True

        elif direction == "down":
            if x + 1 < self.width and self.map[x+1][y] == ".":
                x += 1
                return True
        return False

