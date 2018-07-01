import math

n = 100

factorial = math.factorial(n)
result = sum(int(i) for i in str(factorial))
print(result)