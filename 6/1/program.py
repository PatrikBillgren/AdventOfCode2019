class Node:
    def __init__(self):
        self.children = list()


allNodes = dict()

lines = [line.rstrip('\n') for line in open('input')]
head = None
for line in lines:
    objs = line.split(')')
    node1 = allNodes.get(objs[0], Node())
    allNodes[objs[0]] = node1
    node2 = allNodes.get(objs[1], Node())
    allNodes[objs[1]] = node2
    
    node1.children.append(node2)

    if objs[0] == 'COM':
        head = node1

sum = 0

def traverse(node, level):
    global sum
    sum += level
    for node in node.children:
        traverse(node, level + 1)
traverse(head, 0)
print(sum)

