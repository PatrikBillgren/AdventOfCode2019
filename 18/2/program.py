
filename = 'input'
file = open(filename)
lines = [line.rstrip('\n') for line in file]
file.close()

paths = set()
keys = set()
doors = set()
keyToDoor = dict()
keyToKeyname = dict()
startPoints = list()
minimumPaths = dict()

for i in range(len(lines)):
    line = lines[i]
    for j in range(len(line)):
        point = (j, i)
        char = line[j]
        if char == '.':
            paths.add(point)
        elif char >= 'a' and char <= 'z':
            keys.add(point)
            keyToKeyname[point] = char
        elif char >= 'A' and char <= 'Z':
            doors.add(point)
            keyToDoor[char.lower()] = point
        elif char == '@':
            paths.add(point)
            startPoints.append(point)
        elif char == '#':
            pass

print(f'paths {paths}')
print(f'keys {keys}')
print(f'doors {doors}')
print(f'keyToDoor {keyToDoor}')
print(f'keyToKeyname {keyToKeyname}')

def isUnlockedDoor(foundKeys, pos):
    return any(pos == keyToDoor.get(keyToKeyname[key], (-1, -1)) for key in foundKeys)

allPossibleChoices = dict()
def findAllPossibleChoices(foundKeys, pos):
    if (frozenset(foundKeys), pos) in allPossibleChoices.keys():
        return allPossibleChoices[(frozenset(foundKeys), pos)]

    discoveredKeys = set()
    parents = dict()
    q = list()
    disc = set()
    disc.add(pos)
    q.append(pos)
    while len(q) > 0:
        v = q.pop(0)
        for neighbour in [(v[0] + 1, v[1]), (v[0] - 1, v[1]), (v[0], v[1] + 1), (v[0], v[1] -1)]:
            if (neighbour in paths or neighbour in keys or isUnlockedDoor(foundKeys, neighbour)) and not neighbour in disc:
                disc.add(neighbour)
                parents[neighbour] = v
                if neighbour not in foundKeys and neighbour in keys:
                    discoveredKeys.add(neighbour)
                else:
                    q.append(neighbour)

    choices = set()
    for key in discoveredKeys:
        count = 0
        v = key
        while v != pos:
            v = parents[v]
            count += 1
        choices.add((count, key))
    allPossibleChoices[(frozenset(foundKeys), pos)] = choices
    return choices

def findPath(foundKeys, positions):
    if foundKeys == keys:
        return (0, list())
    if (frozenset(foundKeys), frozenset(positions)) in minimumPaths.keys():
        return minimumPaths[(frozenset(foundKeys), frozenset(positions))]
    minimum = 21474836470000
    chosen = None
    minRes = None
    for i in range(len(positions)):
        pos = positions[i]
        choices = findAllPossibleChoices(foundKeys, pos)
        for choice in choices:
            newKeys = foundKeys.copy()
            newKeys.add(choice[1])
            posCopy = positions.copy()
            del posCopy[i]
            posCopy.insert(i, choice[1])
            res = findPath(newKeys, posCopy)
            if res[0] + choice[0] < minimum:
                minimum = res[0] + choice[0]
                minRes = res
                chosen = choice

    newResList = minRes[1].copy()

    newResList.insert(0, keyToKeyname[chosen[1]])
    retValue = (minimum, newResList)
    minimumPaths[(frozenset(foundKeys), frozenset(positions))] = retValue 
    return retValue

print(findPath(set(), startPoints))
