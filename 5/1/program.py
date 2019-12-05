import sys

lines = [line.rstrip('\n') for line in open('input')]
numbers = list(map(int, lines[0].split(",")))

i = 0

while i < len(numbers):

    opcode = numbers[i]
    if opcode > 100:
        newOpcode = opcode % 100
        mode1 = int(int((opcode % 1000)) / 100)
        mode2 = int(int((opcode % 10000)) / 1000)
        mode3 = int(int((opcode % 100000)) / 10000)
        opcode = newOpcode
        if mode1:
            number1 = numbers[i+1]
        else:
            number1 = numbers[numbers[i+1]]

        if newOpcode in (1, 2):
            if mode2:
                number2 = numbers[i+2]
            else:
                number2 = numbers[numbers[i+2]]
    elif opcode != 99:
        number1 = numbers[numbers[i + 1]]
        if opcode in (1, 2):
            number2 = numbers[numbers[i + 2]]

    if opcode == 99:
        i = len(numbers)
    if opcode == 1 or opcode == 2:
        number3 = numbers[i + 3]
        if (opcode == 1):
            numbers[number3] = number1 + number2
        else:
            numbers[number3] = number1 * number2
        i += 4
    if opcode == 3:
        inputValue = int(input('input'))
        numbers[numbers[i + 1]] = inputValue
        i += 2
    if opcode == 4:
        print(number1)
        i += 2




