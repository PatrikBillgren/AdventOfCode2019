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
        #print(opcode)

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

def printbeam():
    file = open('input')
    lines = [line.rstrip('\n') for line in file]
    file.close()
    numbers = list(map(int, lines[0].split(",")))
    numbers.extend([0] * 10000)
    found = False
    for i in range(500, 1000):
        for j in range(1500, 1600):
            if squarefit(numbers, j, i):
                print(f'Result {j}, {i} result {j * 10000 + i}')
                found = True
                break
        if found:
            break
                
cache = dict()
def run_computer_file_cached(numbers, x, y):
    if (x, y) in cache.keys():
        return cache[(x, y)]
    res = run_computer_file(numbers, x, y)
    cache[(x, y)] = res
    return res

def squarefit(numbers, startx, starty):
    target = 100
    failed = False
    count = 0
    x = startx
    y = starty
    while True:
        out = run_computer_file_cached(numbers, x, y)
        if out == 0:
            failed = count != target
            break
        x += 1
        count += 1
    if failed:
        return False

    count = 0
    x = startx
    y = starty
    while True:
        out = run_computer_file(numbers, x, y)
        if out == 0:
            failed = count != target
            break
        count += 1
        y += 1
    return not failed

def run_computer_file(numbers, x, y):
    inQueue = Queue()
    outQueue = Queue()
    t = Thread(target = run_computer , args = (numbers.copy(), inQueue, outQueue, 0))
    t.start()
    inQueue.put(x)
    inQueue.put(y)
    return outQueue.get()

if __name__ == '__main__':
    printbeam()
