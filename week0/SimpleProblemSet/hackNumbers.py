def is_palindrome(str):
    size = len(str)
    for i in range(size//2):
        if str[i] != str[size - 1 - i]:
            return False
    return True


def odd_number_of_ones(str):
    count = 0
    for char in str:
        if char == "1":
            count += 1
    return count % 2 == 1


def next_hack(n):
    while True:
        n += 1
        binary = bin(n)[2:]
        if is_palindrome(binary) and odd_number_of_ones(binary):
            return n


print(next_hack(8031))
