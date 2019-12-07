import sys
import itertools
from queue import Queue
from threading import Thread

def run_computer(numbers, in_queue, out_queue, num):
    i = 0
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

        if mode1:
            def number1():
                return numbers[i + 1]
        else:
            def number1():
                return numbers[numbers[i + 1]]

        if mode2:
            def number2():
                return numbers[i + 2]
        else:
            def number2():
                return numbers[numbers[i + 2]]
        if mode3:
            def number3():
                return numbers[i + 3]
        else:
            def number3():
                return numbers[numbers[i + 3]]
        if opcode == 99:
            i = len(numbers)
        if opcode == 1 or opcode == 2:
            if (opcode == 1):
                numbers[numbers[i + 3]] = number1() + number2()
            else:
                numbers[numbers[i + 3]] = number1() * number2()
            i += 4
        if opcode == 3:
            inputValue = in_queue.get()
            numbers[numbers[i + 1]] = inputValue
            i += 2
        if opcode == 4:
            out_queue.put(number1())
            i += 2
        if opcode == 5:
            if number1() != 0:
                i = number2()
            else:
                i += 3
        if opcode == 6:
            if number1() == 0:
                i = number2()
            else:
                i += 3
        if opcode == 7:
            if number1() < number2():
                numbers[numbers[i + 3]] = 1
            else:
                numbers[numbers[i + 3]] = 0
            i += 4
        if opcode == 8:
            if number1() == number2():
                numbers[numbers[i + 3]] = 1
            else:
                numbers[numbers[i + 3]] = 0
            i += 4




lines = [line.rstrip('\n') for line in open('input')]
numbers = list(map(int, lines[0].split(",")))
phases = [9, 8, 7, 6, 5]

possibleCombinations = itertools.permutations(phases)
maximum = 0
for perm in possibleCombinations:
    queues = list()
    threads = list()
    for phase in perm:
        queues.append(Queue())
    i = 0
    while i < len(perm):
        queue = queues[i]
        prevQueue = queues[(i - 1) % len(queues)]
        prevQueue.put(perm[i])
        if i == 0:
            prevQueue.put(0)
        t = Thread(target = run_computer , args = (numbers.copy(), prevQueue, queue, i))
        threads.append(t)
        i += 1
    for thread in threads:
        thread.start()
    threads[-1].join()
    out = queues[-1].get()
    if out > maximum:
        maximum = out

print(maximum)
