def sudoku_solved(sudoku):
    if len(sudoku) != 9:
        return False
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        row_numbers = []
        col_numbers = []
        for j in range(9):
            row_numbers.append(sudoku[i][j])
            col_numbers.append(sudoku[j][i])
        row_numbers.sort()
        col_numbers.sort()

        if row_numbers != numbers or col_numbers != numbers:
            return False

    for a in range(0,9,3):
        for b in range(0,9,3):
            square_numbers = []
            for i in range(a,a+3):
                for j in range(b,b+3):
                    square_numbers.append(sudoku[i][j])
            square_numbers.sort()
            if square_numbers != numbers:
                return False
    return True





def main():
    print(sudoku_solved([
        [4, 5, 2, 3, 8, 9, 7, 1, 6],
        [3, 8, 7, 4, 6, 1, 2, 9, 5],
        [6, 1, 9, 2, 5, 7, 3, 4, 8],
        [9, 3, 5, 1, 2, 6, 8, 7, 4],
        [7, 6, 4, 9, 3, 8, 5, 2, 1],
        [1, 2, 8, 5, 7, 4, 6, 3, 9],
        [5, 7, 1, 8, 9, 2, 4, 6, 3],
        [8, 9, 6, 7, 4, 3, 1, 5, 2],
        [2, 4, 3, 6, 1, 5, 9, 8, 7]
        ]))
    print(sudoku_solved([
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ]))

if __name__ == '__main__':
    main()
