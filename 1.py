result = 0
number = 999
for i in range(1,number+1):
    print(i)
    if i % 3 == 0 or i % 5 == 0:
        # print(i)
        result += i
print(result)