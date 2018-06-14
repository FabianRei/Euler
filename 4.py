import itertools

digitNum = 3

def isPalindrome(num):
    return str(num) == str(num)[::-1]

palindromes = []
mi = int('1'+ '0'*(digitNum-1))
ma = mi*10
nums = list(range(mi, ma))
combos = itertools.combinations(nums, 2)
for x, y in combos:
    if isPalindrome(x*y):
        palindromes.append(x*y)

print(palindromes)
print(max(palindromes))