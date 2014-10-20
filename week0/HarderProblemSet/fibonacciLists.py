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
