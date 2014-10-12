from isPrime import is_prime


def prime_number_of_divisors(n):
    n = abs(n)
    numDivisors = 0
    for i in range(1, n+1):
        if n % i == 0:
            numDivisors += 1
    return is_prime(numDivisors)

print (prime_number_of_divisors(7))
print (prime_number_of_divisors(8))
