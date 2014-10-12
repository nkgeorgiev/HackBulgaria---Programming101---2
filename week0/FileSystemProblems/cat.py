import sys


def main():
    filename = sys.argv[1]
    file = open(filename, 'r')

    print(file.read())
    file.close()

if __name__ == '__main__':
    main()
