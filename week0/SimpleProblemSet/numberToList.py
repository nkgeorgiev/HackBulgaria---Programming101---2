def number_to_list(n):
    list = []
    while n > 0:
        list.append(n % 10)
        n //= 10
    list.reverse()
    return list


def main():
    print(number_to_list(123023))

if __name__ == '__main__':
    main()