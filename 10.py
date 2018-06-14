import numpy as np

n = 2000000

def getPrimes(maxNumbers):
    primes = []
    numbers = np.array(list(range(2, maxNumbers)), dtype=np.int64)
    for i in range(len(numbers)):
        n = numbers[i]
        if n == 0:
            continue
        primes.append(n)
        deletionIndexes = []
        # smarter indexing
        num = n - 2
        deletionIndexes.append(num)
        num += n*(n-1)
        while num <= maxNumbers-3:
            deletionIndexes.append(num)
            num += n
        numbers[deletionIndexes] = 0
    return primes

primes = getPrimes(n)
print(primes)
print(np.sum(primes))