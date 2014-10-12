import sys


def main():
    mode = sys.argv[1]
    filename = sys.argv[2]
    with open(filename, "r") as file:
        if mode == "chars":
            text = file.read()
            print(len(text))
        elif mode == "words":
            words = file.read().split(" ")
            for word in words:
                print(word)
            print(len(words))
        elif mode == "lines":
            lines = file.read().split("\n")
            print(len(lines))
        else:
            print("Invalid option!")


if __name__ == '__main__':
    main()
