import sys

lines = [line.rstrip('\n') for line in open('input')]
numbers = list(map(int, lines[0].split(",")))

i = 0
numbers[1] = 12
numbers[2] = 2

while i < len(numbers):
    opcode = numbers[i]
    if (opcode == 99):
        i = len(numbers)
    if (opcode == 1 or opcode == 2):
        number1 = numbers[numbers[i + 1]]
        number2 = numbers[numbers[i + 2]]
        number3 = numbers[i + 3]
        if (opcode == 1):
            numbers[number3] = number1 + number2
        else:
            numbers[number3] = number1 * number2
    i += 4

print(numbers[0])
