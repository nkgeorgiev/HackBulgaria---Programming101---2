from fibonacciLists import nth_fib_lists


def contains(small, big):
    for i in xrange(1 + len(big) - len(small)):
        if small == big[i:i+len(small)]:
            return True
    return False


def member_of_nth_fib_lists(listA, listB, needle):
    a = len(listA)
    b = len(listB)
    fib = 0
    count = 2
    while fib < len(needle):
        fib = a + b
        a = b
        b = fib
        count += 1
    if fib > len(needle):
        return False
    l = nth_fib_lists(listA, listB, count)
    return l == needle


def main():
    print(member_of_nth_fib_lists([1, 2], [3, 4], [1, 2, 3, 4, 3, 4, 1, 2, 3, 4]))
    print(member_of_nth_fib_lists([7, 11], [2], [7, 11, 2, 2, 7, 11, 2]))
    print(member_of_nth_fib_lists([7, 11], [2], [11, 7, 2, 2, 7]))

if __name__ == '__main__':
    main()
