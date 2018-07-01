

with open('p067_triangle.txt') as f:
    triNumberStrings = f.read().splitlines()

triNumbers = []
for numString in triNumberStrings:
    triNumbers.append([int(i) for i in numString.split(' ')])
reversedTri = list(reversed(triNumbers))
for i in range(1, len(reversedTri)):
    newRow = []
    oldRow = reversedTri[i]
    rowBelow = reversedTri[i-1]
    for j, num in enumerate(oldRow):
        newNum = max([num+rowBelow[j], num+rowBelow[j+1]])
        newRow.append(newNum)
    reversedTri[i] = newRow
print(reversedTri[-1])