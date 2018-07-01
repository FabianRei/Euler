from itertools import combinations
import numpy as np
import time

def getAllDivisors(num):
    result = []
    for i in range(2, int(np.sqrt(num))+1):
        if num % i == 0:
            result.append(i)
            result.append(num/i)
    result.append(num)
    result = list(set(result))
    return result


def getDivisors(num, n):
    divisors = []
    if n % 2 == 0:
        divisor1 = n/2
        divisor2 = n+1
    else:
        divisor1 = (n+1)/2
        divisor2 = n
    divisorList1 = getAllDivisors(int(divisor1))
    divisorList2 = getAllDivisors(int(divisor2))
    antiDivisorList1 = [num/n for n in divisorList1]
    antiDivisorList2 = [num/n for n in divisorList2]
    divisors.extend(divisorList1)
    divisors.extend(divisorList2)
    divisors.extend(antiDivisorList1)
    divisors.extend(antiDivisorList2)
    while True:
        divisors = list(set(divisors))
        lenOld = len(divisors)
        divisorArr = np.asarray(divisors)
        combos = combinations(divisorArr[divisorArr<np.round(np.sqrt(num))], 2)
        for combo in combos:
            comboProduct = np.product(combo)
            if num % comboProduct == 0 and not comboProduct in divisors:
                divisors.append(comboProduct)
                if not num//comboProduct in divisors:
                    divisors.append(num//comboProduct)
        if lenOld == len(divisors):
            break
        else:
            pass
            # print("a second time is needed")
    divisors.extend([1, num])
    divisors = list(set(divisors))
    return len(divisors), divisors


# A bit brute force, but it runs within 2 minutes
# I am actually confident to say that this is one of the most elegant brute force methods (if that isn't an oxymoron..)
numDivisors = 500

start = time.time()
for n in range(1,1000000):
    num = n*(n+1)/2
    num = int(num)
    divisors, divisorList = getDivisors(num, n)
    # print('{} has {} divisors'.format(num, divisors))
    if divisors > numDivisors:
        print('{} has {} divisors'.format(num, divisors))
        result = num
        break

print(list(np.sort(divisorList).astype(int)))
end = time.time()

print('took {} seconds to run'.format(end-start))