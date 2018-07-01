import numpy as np

def getSequence(startNum, sequenceLengthsList):
    additum = 0
    sequence = []
    currNum = startNum
    sequence.append(currNum)
    while currNum != 1:
        if currNum % 2 == 0:
            currNum = currNum//2
        else:
            currNum = 3*currNum+1
        if currNum < n and not sequenceLengthsList[currNum] == -1:
            additum = sequenceLengthsList[currNum]
            break
        sequence.append(currNum)
    return np.asarray(sequence), additum


n = 1000000

knownNumbers = []
sequenceLengthsList = list(range(n+1))
sequenceLengthsList = np.asarray(sequenceLengthsList)
sequenceLengthsList[:] = -1
for i in range(2, n):
    if sequenceLengthsList[-1] == -1:
        sequence, additum = getSequence(i, sequenceLengthsList)
    currSequenceLength = len(sequence)
    for j in range(currSequenceLength):
        if sequence[j] < n and sequenceLengthsList[sequence[j]] == -1:
            sequenceLengthsList[sequence[j]] = currSequenceLength - j + additum
        elif sequence[j] < n and not sequenceLengthsList[sequence[j]] == -1:
            break


print(list(sequenceLengthsList).index(max(sequenceLengthsList)))
