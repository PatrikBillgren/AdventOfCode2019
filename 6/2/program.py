import pdb

class Node:
    def __init__(self, name):
        self.children = list()
        self.parent = None
        self.checked = False
        self.name = name

allNodes = dict()

lines = [line.rstrip('\n') for line in open('input')]
head = None
you = None
san = None
for line in lines:
    objs = line.split(')')
    node1 = allNodes.get(objs[0], Node(objs[0]))
    allNodes[objs[0]] = node1
    node2 = allNodes.get(objs[1], Node(objs[1]))
    allNodes[objs[1]] = node2
    
    node1.children.append(node2)
    node2.parent = node1

    if objs[0] == 'COM':
        head = node1
    if objs[0] == 'YOU':
        you = node1
    elif objs[0] == 'SAN':
        san = node1

    if objs[1] == 'YOU':
        you = node2
    elif objs[1] == 'SAN':
        san = node2

sum = 0

def findSan(node, steps):
    if node == san:
        return steps
    node.checked = True
    for child in node.children:
        find = 0
        if not child.checked:
            find = findSan(child, steps + 1)  
        if find != 0:
            return find
    if not node.parent.checked:
        return findSan(node.parent, steps + 1)
    else:
        return 0

print(findSan(you, 0) - 2)

