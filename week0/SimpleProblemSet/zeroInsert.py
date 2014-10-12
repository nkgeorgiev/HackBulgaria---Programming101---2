from numberToList import number_to_list
from listToNumber import list_to_number


def zero_insert(n):
    digits = number_to_list(n)
    i = 0
    while i < len(digits) - 1:
        if digits[i] == digits[i+1] or (digits[i] + digits[i+1]) % 10 == 0:
            digits.insert(i+1, 0)
        i += 1
    return list_to_number(digits)

print(zero_insert(55555555))
