def is_an_bn(word):
    if word == '':
        return True
    a = 0
    if word[0] != 'a':
        return False
    for char in word:
        if char == 'a':
            a += 1
        elif char == 'b':
            break
        else:
            return False
    for i in range(a, len(word)):
        if word[i] != 'b':
            return False
        a -= 1
    return a == 0


def main():
    print(is_an_bn("aaabbb"))
    print(is_an_bn("aabbaabb"))
    print(is_an_bn("rado"))


if __name__ == '__main__':
    main()
