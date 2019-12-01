masses = [line.rstrip('\n') for line in open('input')]
sum = 0
for mass in masses:
    massInt = int(mass)
    while massInt > 0:
        massInt = int(massInt / 3) - 2 
        if massInt > 0:
            sum += massInt
print(sum)

