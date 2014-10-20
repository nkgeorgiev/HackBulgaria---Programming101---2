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

    for a in range(0, 9, 3):
        for b in range(0, 9, 3):
            square_numbers = []
            for i in range(a, a+3):
                for j in range(b, b+3):
                    square_numbers.append(sudoku[i][j])
            square_numbers.sort()
            if square_numbers != numbers:
                return False
    return True
