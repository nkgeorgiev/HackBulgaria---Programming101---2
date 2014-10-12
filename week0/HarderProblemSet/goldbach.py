from isPrime import is_prime


def goldbach(n):
    ans = []
    for i in range(2, n // 2 + 1):
        if is_prime(i) and is_prime(n - i):
            ans.append((i, n - i))
    return ans


def main():
    print(goldbach(100))
    print(goldbach(10))

if __name__ == '__main__':
    main()
