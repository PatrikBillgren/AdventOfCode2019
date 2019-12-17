import sys
import itertools
from queue import Queue
from threading import Thread
import pdb
import random

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
            if inputValue == 99999:
                break
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
    point = (0, 0)
    direction = 0
    directions = [3, 1, 4, 2]
    walls = set()
    paths = set()

    a = 0
    foundPoint = None
    steps = 0
    while t.is_alive() or not outQueue.empty():
        #print(f'direction {direction}')
        inQueue.put(directions[direction])
        oldPoint = point

        if directions[direction] == 1:
            point = (point[0], point[1] + 1)
        elif directions[direction] == 2:
            point = (point[0], point[1] - 1)
        elif directions[direction] == 3:
            point = (point[0] -1, point[1])
        else: 
            point = (point[0] + 1, point[1])

        status = outQueue.get()
        if status == 0: #Wall
            walls.add(point)
            point = oldPoint
            direction = direction = (direction + 1) % 4
        elif status == 1:
            paths.add(point)
            direction = direction = (direction - 1) % 4
            steps += 1
        else:
            foundPoint = point
            paths.add(point)
            break

    inQueue.put(99999)
    for i in range(-50,30):
        for j in range(-50, 50):
            if (j, i) == (0, 0):
                print('D', end='')
            elif (j, i) == foundPoint:
                print('S', end='')
            elif (j, i) in walls:
                print('#', end='')
            elif (j, i) in paths:
                print('.', end='')
            else:
                print(' ', end='')
        print('')

    pathsToCheck = paths.copy()
    checked = set()
    checked.add((0,0))
    parents = dict()
    disc = set()
    Q = list()
    p = (0, 0)
    disc.add(p)
    Q.append(p)
    while len(Q) > 0:
        p = Q.pop(0)
        if p == foundPoint:
            break
        for neighbour in ((p[0], p[1] + 1), (p[0], p[1] - 1), (p[0] + 1, p[1]), (p[0] - 1, p[1])):
            if neighbour in paths and neighbour not in disc:
                disc.add(neighbour)
                parents[neighbour] = p
                Q.append(neighbour)
    print(parents[foundPoint])

    i = 0 
    p = foundPoint
    while True:
        if p == (0, 0):
            break
        p = parents[p]
        i += 1
    print(f'parent count {i}')

    print(f'Status {status}, point {point}, steps {steps}')


if __name__ == '__main__':
    output = run_computer_file('input')
    print(f'program output: {output}')
