from math import sqrt
from operator import mul
from functools import reduce

n = 600851475143
n_orig = n
numbers = list(range(2, int(sqrt(n+1))))
primes = []
for i in range(n):
    while n % numbers[i] == 0:
        num = numbers[i]
        n = n/num
        primes.append(num)
    if n == 1:
        break
    if n % numbers[i] == 0:
        for j in numbers:
            if j % num == 0:
                numbers.remove(j)

print(primes)
print('n is {}, prod of primes is {}'.format(n_orig, reduce(mul, primes, 1)))
print(num)
