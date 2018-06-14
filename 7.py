n = 10001


def getPrimes(maxNumbers):
    primes = []
    numbers = list(range(2, maxNumbers))
    while True:
        try:
            n = numbers[0]
        except IndexError:
            break
        primes.append(n)
        # smart index deleting might make this faster, but I am too lazy and this gives me a result within 3 min
        for num in numbers:
            if num % n == 0:
                numbers.remove(num)
    return primes


# until 5.000.000th prime, there are more than 5% primes in a number sequence starting from 2
primes = getPrimes(n*20)
result = primes[n-1]
print(result)