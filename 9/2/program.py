import sys
import itertools
from queue import Queue
from threading import Thread

def run_computer(numbers, in_queue, out_queue, num):
    i = 0
    relative_base = 0
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

        if mode1 == 1:
            def number1():
                return i + 1
        elif mode1 == 0:
            def number1():
                return numbers[i + 1]
        else:
            def number1():
                return relative_base + numbers[i + 1]

        if mode2 == 1:
            def number2():
                return i + 2
        elif mode2 == 0:
            def number2():
                return numbers[i + 2]
        else:
            def number2():
                return relative_base + numbers[i + 2]

        if mode3 == 1:
            def number3():
                return i + 3
        elif mode3 == 0:
            def number3():
                return numbers[i + 3]
        else:
            def number3():
                return relative_base + numbers[i + 3]


        if opcode == 99:
            i = len(numbers)
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


lines = [line.rstrip('\n') for line in open('input')]
numbers = list(map(int, lines[0].split(",")))
numbers.extend([0] * 10000)

inQueue = Queue()
inQueue.put(2)
outQueue = Queue()
t = Thread(target = run_computer , args = (numbers.copy(), inQueue, outQueue, 0))
t.start()
t.join()
out = 0
while not outQueue.empty():
    print(outQueue.get())
