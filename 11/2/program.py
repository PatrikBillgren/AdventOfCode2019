import sys
import itertools
from queue import Queue
from threading import Thread
import pdb

def _calc_opcode_args(opcode, numbers, i, relative_base):
    modes = list()
    args = list()
    newOpcode = opcode % 100
    modes.append(int(int((opcode % 1000)) / 100))
    modes.append(int(int((opcode % 10000)) / 1000))
    modes.append(int(int((opcode % 100000)) / 10000))
    opcode = newOpcode

    j = 1
    for mode in modes:
        if mode == 1:
            args.append(i + j)
        elif mode == 0:
            args.append(numbers[i + j])
        else:
            args.append(relative_base + numbers[i + j])
        j += 1
    return (opcode, args)


def run_computer(numbers, in_queue, out_queue, num):
    i = 0
    relative_base = 0
    while i < len(numbers):
        opcode, args = _calc_opcode_args(numbers[i], numbers, i, relative_base)
        def number1():
            return args[0]
        def number2():
            return args[1]
        def number3():
            return args[2]

        if opcode == 99:
            break
        if opcode == 1 or opcode == 2:
            if (opcode == 1):
                numbers[number3()] = numbers[number1()] + numbers[number2()]
            else:
                numbers[number3()] = numbers[number1()] * numbers[number2()]
            i += 4
        if opcode == 3:
            inputValue = in_queue.get()
            numbers[number1()] = inputValue
            i += 2
        if opcode == 4:
            out_queue.put(numbers[number1()])
            i += 2
        if opcode == 5:
            if numbers[number1()] != 0:
                i = numbers[number2()]
            else:
                i += 3
        if opcode == 6:
            if numbers[number1()] == 0:
                i = numbers[number2()]
            else:
                i += 3
        if opcode == 7:
            if numbers[number1()] < numbers[number2()]:
                numbers[number3()] = 1
            else:
                numbers[number3()] = 0
            i += 4
        if opcode == 8:
            if numbers[number1()] == numbers[number2()]:
                numbers[number3()] = 1
            else:
                numbers[number3()] = 0
            i += 4
        if opcode == 9:
            relative_base += numbers[number1()]
            i += 2

def run_computer_file(filename):
    file = open(filename)
    lines = [line.rstrip('\n') for line in file]
    file.close()
    numbers = list(map(int, lines[0].split(",")))
    numbers.extend([0] * 10000)

    inQueue = Queue()
    outQueue = Queue()
    t = Thread(target = run_computer , args = (numbers.copy(), inQueue, outQueue, 0))
    t.start()
    blacksquares = set()
    whitesquares = set()

    point = (0, 0)
    whitesquares.add(point)
    direction = 0 # 0 up, 1 right, 2 down, 3 left
    inQueue.put(1)
    while t.is_alive():
        out = outQueue.get()
        if out == 1:
            whitesquares.add(point)
            blacksquares.discard(point)
        else:
            blacksquares.add(point)
            whitesquares.discard(point)
        out = outQueue.get()
        if out == 0:
            direction -= 1
        else:
            direction += 1
        direction = direction % 4
        if direction == 0:
            point = (point[0], point[1] + 1)
        elif direction == 1:
            point = (point[0] + 1, point[1])
        elif direction == 2:
            point = (point[0], point[1] - 1)
        elif direction == 3:
            point = (point[0] - 1, point[1])

        if point in whitesquares:
            inQueue.put(1)
        else:
            inQueue.put(0)
        
    minx = 0
    miny = 0
    maxx = 0
    maxy = 0
    for (x, y) in whitesquares:
        if x < minx:
            minx = x
        if x > maxx:
            maxx = x
        if y < miny:
            miny = y
        if y > maxy:
            maxy = y
    print(f'{minx} {maxx} {miny} {maxy}')

    print(f'{range(maxy + 1, miny - 1)}')
    for i in reversed(range(miny, maxy + 1)):
        for j in range(minx, maxx + 1):
            if (j, i) in whitesquares:
                print('#', end='')
            else:
                print('.', end='')
        print('\n', end='')

    return len(blacksquares)

if __name__ == '__main__':
    output = run_computer_file('input')
    print(f'program output: {output}')
