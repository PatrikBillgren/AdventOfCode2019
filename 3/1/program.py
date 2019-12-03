
lines = [line.rstrip('\n') for line in open('input')]
directions1 = lines[0].split(",")
directions2 = lines[1].split(",")

points1 = set()
points2 = set()

x = 0
y = 0
for direct in directions1:
    direction, steps = direct[:1], int(direct[1:])
    for i in range(steps):
        if direction == 'U':
            y += 1
        elif direction == 'D':
            y -= 1
        elif direction == "L":
            x -= 1
        elif direction == "R":
            x += 1
        points1.add((x, y))

x = 0
y = 0
for direct in directions2:
    direction, steps = direct[:1], int(direct[1:])
    for i in range(steps):
        if direction == 'U':
            y += 1
        elif direction == 'D':
            y -= 1
        elif direction == "L":
            x -= 1
        elif direction == "R":
            x += 1
        points2.add((x, y))

print(points1.intersection(points2))

intersection = points1.intersection(points2)

def manhattanDistance(point):
    return abs(point[0]) + abs(point[1])

print(manhattanDistance(min(intersection, key=manhattanDistance)))
