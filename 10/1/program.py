from math import sqrt

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

    def __repr__(self):
        return f'Vector x:{self.x} y:{self.y}'

def collinear(a, b):
    if a.y == 0 and b.y == 0 and a.x * b.x > 0:
        return True
    if a.x == 0 and b.x == 0 and a.y * b.y > 0:
        return True
    if a.y == 0 or b.y == 0:
        return False
    return a.x/a.y == b.x/b.y and a.x * b.x > 0 and a.y * b.y > 0

def numberCollinear(point, points):
    found = set()
    foundVectors = set()
    for other_point in points:
        if point == other_point:
            continue
        vector = Vector(point, other_point)
        found = False
        #print(f'{vector}')
        for foundVector in foundVectors:
            if collinear(vector, foundVector):
                #print(f'{vector} {foundVector}')
                found = True
        if not found:
            foundVectors.add(vector)
    return len(foundVectors)


if __name__ == '__main__':
    lines = [line.rstrip('\n') for line in open('input')]
    points = list()
    i = 0
    for line in lines:
        j = 0
        for char in line:
            if char == '#':
                points.append(Point(i, j))
            j += 1
        i += 1



    print(points)
    largest = 0
    largestPoint = None
    for point in points:
        number = numberCollinear(point, points)
        if number > largest:
            largest = number
            largestPoint = point

    print(largest)
    print(largestPoint)
    print(points.index(largestPoint))



