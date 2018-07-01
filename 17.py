from num2words import num2words

# Writing my own num2words function seems boring..
n  = 1000
letterSum = 0
for i in range(1, n+1):
    letters = num2words(i)
    letters = letters.replace(' ', '').replace('-', '')
    letterSum += len(letters)

print(letterSum)
