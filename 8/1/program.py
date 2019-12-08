import textwrap

lines = [line.rstrip('\n') for line in open('input')]
digits = lines[0]
sum = 0

width = 25
length = 6

layers = textwrap.wrap(digits, width * length)

minZero = 1000
result = 0
for layer in layers:
    zeros = layer.count('0')
    if zeros < minZero:
        minZero = zeros
        result = layer.count('1') * layer.count('2')

print(result)

