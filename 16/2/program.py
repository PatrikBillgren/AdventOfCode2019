import math

filename = 'input'
file = open(filename)
lines = [line.rstrip('\n') for line in file]
file.close()
line = list(lines[0])
line = line * 10000

offset = int(''.join(line[:7]))
length = len(line)
print(f'offset: {offset}')
print(f'length {len(line)}')

line = line[offset:]
for _ in range(100):
    for i in reversed(range(len(line))):
        if not i == len(line) - 1:
            line[i] = (int(line[i]) + int(line[i + 1])) % 10
    

for i in line[:8]:
    print(i, end='')
print()
