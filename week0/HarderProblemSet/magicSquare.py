def magic_square(matrix):
    sum = 0
    n = len(matrix)
    for i in range(n):
        sum += matrix[i][0]
    for i in range(n):
        col_sum = 0
        row_sum = 0
        for j in range(n):
            col_sum += matrix[j][i]
            row_sum += matrix[i][j]
        if col_sum != sum or row_sum != sum:
            return False
    first_diagonal = 0
    second_diagonal = 0
    for i in range(n):
        first_diagonal += matrix[i][i]
        second_diagonal += matrix[n - i - 1][i]
    if first_diagonal != sum or second_diagonal != sum:
        return False
    return True

def main():
    print(magic_square([[7,12,1,14], [2,13,8,11], [16,3,10,5], [9,6,15,4]]))
    print(magic_square([[1,2,3], [4,5,6], [7,8,9]]))
    print(magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]]))
    print(magic_square([[4,9,2], [3,5,7], [8,1,6]]))

if __name__ == '__main__':
    main()
