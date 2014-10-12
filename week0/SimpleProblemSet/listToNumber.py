def list_to_number(digits):
    digits.reverse()
    number = 0
    for i in range(len(digits)):
        number += digits[i] * (10 ** i)
    return number


def main():
    print(list_to_number([1, 2, 3, 0, 2, 3]))

if __name__ == '__main__':
    main()
