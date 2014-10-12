def is_int_palindrome(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    size = len(digits)
    for i in range(size//2):
        if digits[i] != digits[size-i-1]:
            return False
    return True

print(is_int_palindrome(123))
