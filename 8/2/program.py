import textwrap

lines = [line.rstrip('\n') for line in open('input')]
digits = lines[0]
sum = 0

width = 25
length = 6

layers = textwrap.wrap(digits, 25 * 6)

minZero = 1000
result = 0
pixels = list()
for pix in range(width * length):
    for layer in layers:
        color = layer[pix]
        if color == '0' or color == '1':
            pixels.append(color)
            break

            
for pix in range(len(pixels)):
    if (pix % width == 0):
        print()
    if pixels[pix] == '0':
        print(' ', end='')
    else:
        print('x', end='')

print()

