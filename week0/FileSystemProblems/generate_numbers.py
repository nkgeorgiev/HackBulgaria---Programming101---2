# generate_numbers.py
import sys
from random import randint


def main():
    filename = sys.argv[1]
    num = int(sys.argv[2])
    file = open(filename,'w')
    numbers = []
    for i in range(num):
        numbers.append(str(randint(1, 1000)))
    file.write(' '.join(numbers))
    file.close()


if __name__ == '__main__':
    main()
