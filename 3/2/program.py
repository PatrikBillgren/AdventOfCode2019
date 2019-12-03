
lines = [line.rstrip('\n') for line in open('input')]
directions1 = lines[0].split(",")
directions2 = lines[1].split(",")

points1 = set()
points2 = set()
pointsToLength1 = dict()
pointsToLength2 = dict()

def calc(directions, points, pointsToLength):
    x = 0
    y = 0
    length = 0
    for direct in directions:
        direction, steps = direct[:1], int(direct[1:])
        for i in range(steps):
            length += 1
            if direction == 'U':
                y += 1
            elif direction == 'D':
                y -= 1
            elif direction == "L":
                x -= 1
            elif direction == "R":
                x += 1
            points.add((x, y))
            if pointsToLength.get((x,y)) == None:
                pointsToLength[(x,y)] = length

calc(directions1, points1, pointsToLength1)
calc(directions2, points2, pointsToLength2)

intersection = points1.intersection(points2)

def signal(point):
    return pointsToLength1[point] + pointsToLength2[point]

print(signal(min(intersection, key=signal)))
