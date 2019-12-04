def checkDigit(number):
    numberAsString = str(number)

    lastDigit = int(numberAsString[0])
    numberDict = dict()

    for char in numberAsString:
        currDigit = int(char)

        if currDigit < lastDigit:
            return False

        numberDict[char] = numberDict.get(char, 0) + 1

        lastDigit = currDigit

    return 2 in numberDict.values()

result = 0
for x in range(108457, 562041):
    if checkDigit(x):
        result += 1

print(result)
