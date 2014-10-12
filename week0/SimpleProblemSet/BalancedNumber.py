def is_number_balanced(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    first_sum = 0
    second_sum = 0
    size = len(digits)
    for i in range(size):
        if i < size // 2:
            first_sum += digits[i]
        elif i > size // 2:
            second_sum += digits[i]
    return first_sum == second_sum

print(is_number_balanced(28471))
