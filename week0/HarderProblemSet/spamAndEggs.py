def prepare_meal(number):
    count = 0
    while number % 3 == 0:
        count += 1
        number //= 3
    str = "spam "*count

    if number % 5 == 0:
        str += "and eggs"
    return str


def main():
    print(prepare_meal(15))


if __name__ == '__main__':
    main()
