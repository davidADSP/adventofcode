import numpy as np
from classes import Node

def count_paths_from(node, visited, double_cave):
    if node.id == 'end':
        paths = 1
    else:
        paths = 0
        for n in node.neighbours:
            if n.id == 'start':
                pass
            elif not n.small:
                paths += count_paths_from(n, visited + [n.id], double_cave)
            elif n.id in visited:
                if not double_cave:
                    paths += count_paths_from(n, visited + [n.id], True)  
            else:
                paths += count_paths_from(n, visited + [n.id], double_cave)
    return paths

# Get data
links = [x.split('-') for x in open("input.txt", "r").read().splitlines()]
nodes = {}

for a, b in links:
    if a not in nodes: nodes[a] = Node(a)
    if b not in nodes: nodes[b] = Node(b)
    nodes[a].neighbours.append(nodes[b])
    nodes[b].neighbours.append(nodes[a])

# Calculate
print(count_paths_from(nodes['start'], visited = ['start'], double_cave = False))

