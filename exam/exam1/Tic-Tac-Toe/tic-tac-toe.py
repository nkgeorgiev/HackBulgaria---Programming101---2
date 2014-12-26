class TicTacToe:
    def __init__(self):
        self.__board = [["-", "-", "-"],
                        ["-", "-", "-"],
                        ["-", "-", "-"]]
        self.__sides = [(0, 1), (1, 0), (2, 1), (1, 2)]
        self.__corners = [(0, 0), (0, 2), (2, 0), (2, 2)]

    def __get_free_squares(self):
        free_squares = []
        for i in len(3):
            for j in len(3):
                if self.__board[i][j] == '-':
                    free_squares.append((i,j))


    def can_win(self):
        free

    def pprint(self):
        for line in self.__board:
            print(line)


t = TicTacToe()
t.pprint()
