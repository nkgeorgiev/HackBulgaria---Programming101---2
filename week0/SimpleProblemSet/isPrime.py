def is_prime(n):
    n = abs(n)
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def main():
    print (is_prime(5))
    print (is_prime(12))

if __name__ == '__main__':
    main()
