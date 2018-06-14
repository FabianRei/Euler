n = 100
sumSquares = 0
squaresSum = 0
for i in range(1, n+1):
    sumSquares += i*i
    squaresSum += i

result = squaresSum*squaresSum - sumSquares
print(result)