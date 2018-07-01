

n = 20
savedForIndex = []
savedResults = []
def findPaths(n, x=0, y=0):
    inputTuple = (n, x, y)
    if inputTuple in savedForIndex:
        return savedResults[savedForIndex.index(inputTuple)]
    if x < n and y < n:
        result = findPaths(n, x+1, y) + findPaths(n, x, y+1)
        savedForIndex.append(inputTuple)
        savedResults.append(result)
        return result
    else:
        return 1


print(findPaths(n))