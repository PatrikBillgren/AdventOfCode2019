masses = [line.rstrip('\n') for line in open('input')]
sum = 0
for mass in masses:
    sum += int(int(mass) / 3) - 2 
print(sum)

