def sum_of_digits(n):
    n = abs(n)
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10

    return sum


def main():
    print (sum_of_digits(1325132435356))
    print (sum_of_digits(-10))

if __name__ == '__main__':
    main()
