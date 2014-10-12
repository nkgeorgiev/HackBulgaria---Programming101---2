import sys


def main():
    filenames = sys.argv[1:]
    with open("MEGATRON.txt", "a+b") as output_file:
        for filename in filenames:
            with open(filename, "r") as input_file:
                output_file.write(input_file.read())
                output_file.write("\n")


if __name__ == '__main__':
    main()
