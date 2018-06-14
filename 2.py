# Fibonacci numbers

n = 4000000

fibonacci_list = [1, 2]
result = 0
i = 1
j = 2
while True:
    fibonacci_list.append(i+j)
    if i>j:
        j = i+j
    else:
        i = j+i
    if i+j > n:
        break

for val in fibonacci_list:
    if val % 2 == 0:
        result += val

print(result)