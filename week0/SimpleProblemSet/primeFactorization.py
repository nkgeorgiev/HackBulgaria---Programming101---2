def prime_factorization(n):
    factor = {}
    a = 2
    while n > 1:
        count = 0
        for i in range(a, n + 1):
            if n % i == 0:
                a = i
                break
        while n % a == 0:
            n //= a
            count += 1
        factor[a] = count
    answer = []
    for num in factor:
        answer.append((num, factor[num]))
    return answer

print(prime_factorization(356))
