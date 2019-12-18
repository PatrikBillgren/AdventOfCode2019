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
    numbers[0] = 2

    inQueue = Queue()
    outQueue = Queue()
    t = Thread(target = run_computer , args = (numbers.copy(), inQueue, outQueue, 0))
    t.start()

    scaffolds = set()
    spaces = set()
    i = 0
    j = 0
    maxi = 0
    maxj = 0
    startPoint = None
    # 76 = L
    # 82 = R
    # 56 = 8
    ORDER = [66, 44, 67, 44, 66, 44, 67, 44, 65, 44, 67, 44, 66, 44, 65, 44, 67, 44, 65, 10]
    A = [82, 44, 49, 48, 44, 76, 44, 56, 44, 76, 44, 52, 44, 82, 44, 49, 48, 10]
    B = [76, 44, 49, 50, 44, 76, 44, 56, 44, 82, 44, 49, 48, 44, 82, 44, 49, 48, 10]
    C = [76, 44, 54, 44, 76, 44, 52, 44, 76, 44, 49, 50, 10]
    for a in ORDER:
        inQueue.put(a)
    for a in A:
        inQueue.put(a)
    for a in B:
        inQueue.put(a)
    for a in C:
        inQueue.put(a)


    inQueue.put(110) # n
    #inQueue.put(121) # y
    inQueue.put(10)
    direction = 0 # 0 = UP, 1 = RIGHT, 2 = DOWN, 3 = LEFT
    while t.is_alive() or not outQueue.empty():
        out = outQueue.get()
        if out == 35:
            scaffolds.add((j, i))
            print('#', end='')
        elif out == 46:
            spaces.add((j, i))
            print('.', end='')
        elif out == 60 or out == 62 or out == 94 or out == 118:
            startPoint = (j, i)
            scaffolds.add((j, i))
            if out == 60:
                direction = 3
                print('<', end='')
            elif out == 62:
                direction = 1
                print('>', end='')
            elif out == 118:
                direction = 2
                print('v', end='')
            else:
                print('^', end='')
        elif out == 10:
            j = 0
            i += 1
            print()
            if i > maxi:
                maxi = i
            continue
        elif out < 150:
            print(str(chr(out)), end='')
        else:
            print(out)
        j += 1
        if j > maxj:
            maxj = j

    print()
    intersections = set()
    for scaffold in scaffolds:
        numNeighbours = 0
        for neighbour in ((scaffold[0], scaffold[1]+1), (scaffold[0], scaffold[1]-1), (scaffold[0]+1, scaffold[1]), (scaffold[0]-1, scaffold[1])):
            if neighbour in scaffolds:
                numNeighbours += 1
        if numNeighbours == 4:
            intersections.add(scaffold)

    currpoint = startPoint
    pointsToVisit = scaffolds.copy()
    pointsToVisit.remove(currpoint)
    intersectionsToVisit = intersections.copy()
    def left(point, direction):
        if direction == 0:
            return (point[0] - 1, point[1])
        if direction == 1:
            return (point[0], point[1] - 1)
        if direction == 2:
            return (point[0] + 1, point[1])
        if direction == 3:
            return (point[0], point[1] + 1)

    def right(point, direction):
        return left(point, (direction + 2) % 4)

    def forward(point, direction):
        return left(point, (direction + 1) % 4)

    def findPath(currpoint, direction, pointsToVisit, intersectionsToVisit):
        count = 0
        path = list()
        while len(pointsToVisit) > 0:
            if forward(currpoint, direction) in pointsToVisit:
                currpoint = forward(currpoint, direction)
                count += 1
            elif left(currpoint, direction) in pointsToVisit:
                currpoint = left(currpoint, direction)
                direction = (direction - 1) % 4
                if count > 0:
                    path.append(count)
                count = 1
                path.append('L')
            elif right(currpoint, direction) in pointsToVisit:
                currpoint = right(currpoint, direction)
                direction = (direction + 1) % 4
                if count > 0:
                    path.append(count)
                count = 1
                path.append('R')


                
            if currpoint in intersectionsToVisit:
                intersectionsToVisit.remove(currpoint)
            elif len(pointsToVisit) > 0:
                pointsToVisit.remove(currpoint)
        path.append(count)
        print(path)
    findPath(currpoint, direction, pointsToVisit, intersectionsToVisit)

if __name__ == '__main__':
    output = run_computer_file('input')
    print(f'program output: {output}')
