import sys


def main():
    args = sys.argv[1:]
    for arg in args:
        file = open(arg, 'r')
        print(file.read())
        file.close()

if __name__ == '__main__':
    main()
