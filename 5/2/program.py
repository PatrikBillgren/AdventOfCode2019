import sys

lines = [line.rstrip('\n') for line in open('input')]
numbers = list(map(int, lines[0].split(",")))

i = 0

while i < len(numbers):

    opcode = numbers[i]
    mode1 = 0
    mode2 = 0
    mode3 = 0
    if opcode > 100:
        newOpcode = opcode % 100
        mode1 = int(int((opcode % 1000)) / 100)
        mode2 = int(int((opcode % 10000)) / 1000)
        mode3 = int(int((opcode % 100000)) / 10000)
        opcode = newOpcode

    if mode1:
        def number1():
            return numbers[i + 1]
    else:
        def number1():
            return numbers[numbers[i + 1]]

    if mode2:
        def number2():
            return numbers[i + 2]
    else:
        def number2():
            return numbers[numbers[i + 2]]
    if mode3:
        def number3():
            return numbers[i + 3]
    else:
        def number3():
            return numbers[numbers[i + 3]]

    if opcode == 99:
        i = len(numbers)
        

    if opcode == 1 or opcode == 2:
        if (opcode == 1):
            numbers[numbers[i + 3]] = number1() + number2()
        else:
            numbers[numbers[i + 3]] = number1() * number2()
        i += 4
    if opcode == 3:
        inputValue = int(input('input'))
        numbers[numbers[i + 1]] = inputValue
        i += 2
    if opcode == 4:
        print(number1())
        i += 2
    if opcode == 5:
        if number1() != 0:
            i = number2()
        else:
            i += 3
    if opcode == 6:
        if number1() == 0:
            i = number2()
        else:
            i += 3
    if opcode == 7:
        if number1() < number2():
            numbers[numbers[i + 3]] = 1
        else:
            numbers[numbers[i + 3]] = 0
        i += 4
    if opcode == 8:
        if number1() == number2():
            numbers[numbers[i + 3]] = 1
        else:
            numbers[numbers[i + 3]] = 0
        i += 4




