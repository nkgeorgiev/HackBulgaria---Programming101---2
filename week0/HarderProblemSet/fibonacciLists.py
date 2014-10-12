def nth_fib_lists(listA, listB, n):
    a = listA
    b = listB
    if n == 1:
        return listA
    if n == 2:
        return listB
    for i in range(n - 2):
        fib = a + b
        a = b
        b = fib
    return fib


def main():
    print(nth_fib_lists([], [1, 2, 3], 4))
    print(nth_fib_lists([], [], 100))

if __name__ == '__main__':
    main()

