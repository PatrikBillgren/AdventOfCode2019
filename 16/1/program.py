import math

filename = 'input'
file = open(filename)
lines = [line.rstrip('\n') for line in file]
file.close()
line = list(lines[0])

def print_first_8(nums):
    for i in range(8):
        print(nums[i], end='')
    print()

sequence = [0, 1, 0, -1]
for _ in range(100):
    output = []
    for digit_index in range(len(line)):
        out = list()
        sequence_index = 1
        sum = 0
        curr_sequence = [seq_elem for seq_list in [[char] * (digit_index + 1) for char in sequence] for seq_elem in seq_list]
        for digit in line:
            result = int(digit) * curr_sequence[sequence_index]
            sum += result
            sequence_index = (sequence_index + 1) % len(curr_sequence)

        sum = abs(sum) %10
        output.append(sum)
    line = output
print_first_8(line)

