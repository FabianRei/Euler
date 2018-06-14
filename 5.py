from operator import mul
from functools import reduce

n = 30


def getPrimesPlusAdditionalMultiplicators(n):
    numbers = list(range(2, n+1))
    primes = []
    while True:
        try:
            n = numbers[0]
        except IndexError:
            break
        primes.append(n)
        for num in numbers:
            if num % n == 0:
                if num/n == 1:
                    numbers.remove(num)
                else:
                    numbers[numbers.index(num)] = num/n

    return primes


primes = getPrimesPlusAdditionalMultiplicators(n)
result = reduce(mul, primes)
print(int(result))