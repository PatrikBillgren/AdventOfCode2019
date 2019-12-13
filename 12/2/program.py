import math

def calc_moons(filename):
    file = open(filename)
    lines = [line.rstrip('\n') for line in file]
    file.close()
    positions = list()
    for line in lines:
        line_split = line.split("=")
        x = int(line_split[1].split(',')[0])
        y = int(line_split[2].split(',')[0])
        z = int(line_split[3].split('>')[0])
        positions.append([x, y, z])
    print(f'Original\n{positions}')
    
    positions_per_axis = (
        [positions[i][0] for i in range(len(positions))],
        [positions[i][1] for i in range(len(positions))],
        [positions[i][2] for i in range(len(positions))])
    counts = list()
    for pos in positions_per_axis:
        velocities = [0 for _ in range(len(pos))]
        count = int(find_repeating_pos(pos, velocities))
        print(f'count {count}')
        counts.append(count)

    print(counts)
    print(lcm3(counts[0], counts[1], counts[2]))

def lcm3(a, b, c):
    return lcm2(lcm2(a, b), c)

def lcm2(a, b):
    return int(a * b / math.gcd(a, b))

def find_repeating_pos(positions, velocities):
    previous = set()
    previous.add((*positions, ))
    orig = positions.copy()
    count = 0
    while velocities != [0 for _ in range(len(velocities))] or positions != orig or count == 0:
        previous.add((*positions, ))
        for i in range(len(positions)):
            for j in range(len(positions)):
                if i == j:
                    continue
                if positions[i] > positions[j]:
                    velocities[i] -= 1
                elif positions[i] < positions[j]:
                    velocities[i] += 1
        for i in range(len(velocities)):
            positions[i] += velocities[i]
        count += 1
    return count 

if __name__ == '__main__':
    calc_moons('input')
