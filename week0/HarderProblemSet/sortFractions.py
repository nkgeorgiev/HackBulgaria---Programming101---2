def sort_fractions(fractions):
    denum = 1
    for item in fractions:
        denum *= item[1]

    return sorted(fractions, key=lambda x: x[0] * (denum // x[1]))


def main():
    print(sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]))
    print(sort_fractions([(2, 3), (1, 2), (1, 3)]))

if __name__ == '__main__':
    main()
