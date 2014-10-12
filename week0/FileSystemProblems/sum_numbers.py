import sys


def main():
    filename = sys.argv[1]
    file = open(filename, 'r')
    numbers = file.read().split(" ")
    sum = 0
    for number in numbers:
        sum += int(number)
    print(sum)
    file.close()

if __name__ == '__main__':
    main()
