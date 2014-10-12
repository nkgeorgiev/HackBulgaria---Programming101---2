def sum_matrix(m):
    sum = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            sum += m[i][j]
    return sum


def main():
    print(sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))
    print(sum_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))

if __name__ == '__main__':
    main()
