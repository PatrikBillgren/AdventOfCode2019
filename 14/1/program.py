import math

filename = 'input'
file = open(filename)
lines = [line.rstrip('\n') for line in file]
file.close()

recipes = dict()
amounts = dict()
rest = dict()

for line in lines:
    equation = line.split(' => ')
    inpsplit = equation[0].split(', ')
    out = equation[1].split(' ')
    outNum = int(out[0])
    outName = out[1]
    inpList = list()
    for inp in inpsplit:
        inpNumName = inp.split(' ')
        inpNum = int(inpNumName[0])
        inpName = inpNumName[1]
        inpList.append((inpNum, inpName))

    recipes[outName] = inpList
    amounts[outName] = outNum
    rest[outName] = 0
    

def findOre(name, number):
    if name == 'ORE':
        return number
    else:
        tot = 0
        amount = amounts[name]
        needed = number - rest[name]
        if needed > 0:
            multiple = int(math.ceil(needed / amount))
            for recipe in recipes[name]:
                tot += findOre(recipe[1], multiple * recipe[0])
            rest[name] = multiple * amount - needed
            tot = tot
        else:
            rest[name] = rest[name] - number
        return  tot

print(findOre('FUEL', 1))
