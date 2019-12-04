
def checkDigit(number):
    numberAsString = str(number)

    lastDigit = int(numberAsString[0])
    hasSeenTwo = False

    for char in numberAsString[1:]:
        currDigit = int(char)
        if currDigit == lastDigit:
            hasSeenTwo = True
        elif currDigit < lastDigit:
            return False
        lastDigit = currDigit

    return hasSeenTwo
        
result = 0
for x in range(108457, 562041):
    if checkDigit(x):
        result += 1

print(result)
