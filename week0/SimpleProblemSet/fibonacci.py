def nth_fibonacci(n):
    a = 1
    b = 1
    fib = 0
    if n in [1, 2]:
        return 1
    for i in range(n-2):
        fib = a + b
        a = b
        b = fib
    return fib

print (nth_fibonacci(1))
print (nth_fibonacci(2))
print (nth_fibonacci(3))
print (nth_fibonacci(10))
