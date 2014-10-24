from orc import Orc
from fight import Fight


class Dungeon:
    def __init__(self, filepath):
        self.map = self.__set_map(filepath)
        self.players = {}
        self.height = len(self.map)
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

    def move_right(self, player_name, x, y, t):
        player = self.players[player_name][0]
        if y + 1 > self.width:
            return False
        if self.map[x][y+1] == '.':
            y += 1
            self.map[x][y] = t
            self.map[x][y-1] = '.'
            return True
        if self.map[x][y+1] in ["H", "O"]:
            enemy_name = self.get_player_by_coordinates(x, y+1)
            enemy = self.players[enemy_name][0]
            result = Fight(player, enemy).simulate_fight()
            y += 1
            if result:
                self.map[x][y] = t
                self.map[x][y-1] = '.'
                del self.players[enemy_name]
            else:
                self.map[x][y-1] = '.'
                del self.players[player_name]
            return True

        return False

    def move_left(self, player_name, x, y, t):
        player = self.players[player_name][0]
        if y - 1 <= 0:
            return False
        if self.map[x][y-1] == '.':
            y -= 1
            self.map[x][y] = t
            self.map[x][y+1] = '.'
            return True
        if self.map[x][y-1] in ["H", "O"]:

            enemy_name = self.get_player_by_coordinates(x, y-1)
            enemy = self.players[enemy_name][0]
            result = Fight(player, enemy).simulate_fight()
            y -= 1
            if result:
                self.map[x][y] = t
                self.map[x][y+1] = '.'
                del self.players[enemy_name]
            else:
                self.map[x][y+1] = '.'
                del self.players[player_name]
            return True

        return False

    def move_up(self, player_name, x, y, t):
        player = self.players[player_name][0]
        if x - 1 <= 0:
            return False
        if self.map[x-1][y] == '.':
            x -= 1
            self.map[x][y] = t
            self.map[x+1][y] = '.'
            return True
        if self.map[x-1][y] in ["H", "O"]:

            enemy_name = self.get_player_by_coordinates(x-1, y)
            enemy = self.players[enemy_name][0]
            result = Fight(player, enemy).simulate_fight()
            x -= 1
            if result:
                self.map[x][y] = t
                self.map[x+1][y] = '.'
                del self.players[enemy_name]
            else:
                self.map[x+1][y] = '.'
                del self.players[player_name]
            return True

        return False

    def move_down(self, player_name, x, y, t):
        player = self.players[player_name][0]
        if x + 1 >= self.height:
            return False
        if self.map[x+1][y] == '.':
            x += 1
            self.map[x][y] = t
            self.map[x-1][y] = '.'
            return True
        if self.map[x+1][y] in ["H", "O"]:

            enemy_name = self.get_player_by_coordinates(x+1, y)
            enemy = self.players[enemy_name][0]
            result = Fight(player, enemy).simulate_fight()
            x += 1
            if result:
                self.map[x][y] = t
                self.map[x-1][y] = '.'
                del self.players[enemy_name]
            else:
                self.map[x-1][y] = '.'
                del self.players[player_name]
            return True

        return False

    def move(self, player_name, direction):
        player = self.players[player_name]
        x = player[1]
        y = player[2]
        t = self.map[x][y]

        if direction == "right":
            return self.move_right(player_name, x, y, t)

        elif direction == "left":
            return self.move_left(player_name, x, y, t)

        elif direction == "up":
            return self.move_up(player_name, x, y, t)

        elif direction == "down":
            return self.move_down(player_name, x, y, t)

    def get_player_by_coordinates(self, x, y):
        for player in self.players.keys():
            if self.players[player][1] == x and self.players[player][2] == y:
                return player
        return False
