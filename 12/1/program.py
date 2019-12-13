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
    velocities = [[0 for _ in range(3)] for _ in range(len(positions))]
    print(f'Original\n{positions}')
    for i in range(1000):
        update(positions, velocities)
    print_result(positions, velocities)

def print_result(positions, velocities):
    sum = 0
    for i in range(len(positions)):
        pos = positions[i]
        vel = velocities[i]
        posTot = 0
        velTot = 0
        for j in range(len(pos)):
            posTot += abs(pos[j])
            velTot += abs(vel[j])
        sum += posTot * velTot
    print(f'Sum {sum}')

def update(positions, velocities):
    for i in range(len(positions)):
        for j in range(len(positions)):
            if i == j:
                continue
            pos1 = positions[i]
            pos2 = positions[j]
            for k in range(3):
                if pos1[k] > pos2[k]:
                    velocities[i][k] -= 1
                elif pos1[k] < pos2[k]:
                    velocities[i][k] += 1
    for i in range(len(positions)):
        pos = positions[i]
        for j in range(len(pos)):
            pos[j] += velocities[i][j]
                



if __name__ == '__main__':
    calc_moons('input')
