from math import sqrt
import sys
import copy

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point x:{self.x} y:{self.y}'

class Vector:
    def __init__(self, pointa, pointb):
        self.x = pointb.x - pointa.x
        self.y = pointb.y - pointa.y
        self.length = sqrt(self.x * self.x + self.y * self.y)

    def abs(self):
        self.x = abs(self.x)
        self.y = abs(self.y)

    def switch(self):
        temp = self.x
        self.x = self.y
        self.y = temp

    def __repr__(self):
        return f'Vector x:{self.x} y:{self.y} length:{self.length}'

    def angle(self):
        if self.x == 0:
            return 0.0
        elif self.y == 0:
            return sys.maxsize
        else:
            return self.x/self.y

def findVectors(point, points):
    foundVectors = set()
    for other_point in points:
        if point == other_point:
            continue
        vector = Vector(point, other_point)
        foundVectors.add(vector)
    return foundVectors

def printPoint(origPoint, vector, quarter):
    x = 0
    y = 0
    if quarter == 0:
        x = origPoint.x + vector.x
        y = origPoint.y - vector.y
    if quarter == 1:
        x = origPoint.x + vector.y
        y = origPoint.y + vector.x
    if quarter == 2:
        x = origPoint.x - vector.x
        y = origPoint.y + vector.y
    if quarter == 3:
        x = origPoint.x - vector.y
        y = origPoint.y - vector.x
    print(f'Vaporised: x: {x} y: {y}')
    print(f'Output: {x * 100 + y}')

def find200th(point, points):
    collinears = findVectors(point, points)
    UR = dict()
    DR = dict()
    DL = dict()
    UL = dict()
    for vector in collinears:
        if vector.x >= 0 and vector.y <= 0:
            vector.abs()
            UR.setdefault(vector.angle(), list()).append(vector)
        elif vector.x >= 0:
            vector.switch()
            vector.abs()
            DR.setdefault(vector.angle(), list()).append(vector)
        elif vector.y > 0:
            vector.abs()
            DL.setdefault(vector.angle(), list()).append(vector)
        else:
            vector.abs()
            vector.switch()
            UL.setdefault(vector.angle(), list()).append(vector)

    quarters = [UR, DR, DL, UL]
    i = 0
    quarter = -1
    output = list()
    while any(quarters):
        quarter += 1
        quarter = quarter % len(quarters)
        qu = quarters[quarter]
        sortedv = sorted(list(qu.items()), key=lambda tup: tup[0]) 
        for keypair in sortedv:
            vectors = sorted(keypair[1], key=lambda vector: vector.length)
            vector = vectors.pop(0)
            qu[keypair[0]] = vectors
            output.append(vector)
            if len(vectors) == 0:
                del qu[keypair[0]]
            if i == 199:
                printPoint(point, vector, quarter)
                return output[-1]
            i += 1
        quarters[quarter] = qu

    return output[-1]

if __name__ == '__main__':
    lines = [line.rstrip('\n') for line in open('input')]
    points = list()
    i = 0
    for line in lines:
        j = 0
        for char in line:
            if char == '#':
                points.append(Point(j, i))
            j += 1
        i += 1

    point = points[237]
    find200th(point, points)

