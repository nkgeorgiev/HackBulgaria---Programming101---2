from containsDigit import contains_digit


def contains_digits(number, digits):
    for digit in digits:
        if not contains_digit(number, digit):
            return False
    return True

print(contains_digits(402123, [0, 3, 4]))
print(contains_digits(123456789, [1, 2, 3, 0]))
