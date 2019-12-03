
lines = [line.rstrip('\n') for line in open('input')]
directions1 = lines[0].split(",")
directions2 = lines[1].split(",")

points1 = set()
points2 = set()

x = 0
y = 0
length = 0
pointsToLength1 = dict()
for direct in directions1:
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
        points1.add((x, y))
        if pointsToLength1.get((x,y)) == None:
            pointsToLength1[(x,y)] = length

x = 0
y = 0
length = 0
pointsToLength2 = dict()
for direct in directions2:
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
        points2.add((x, y))
        if pointsToLength2.get((x,y)) == None:
            pointsToLength2[(x,y)] = length

intersection = points1.intersection(points2)

def signal(point):
    return pointsToLength1[point] + pointsToLength2[point]

print(signal(min(intersection, key=signal)))
