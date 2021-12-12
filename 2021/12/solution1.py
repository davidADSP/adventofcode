import numpy as np
from classes import Node

def count_paths_from(node, visited):
    if node.id == 'end':
        paths = 1
    else:
        paths = 0
        for n in node.neighbours:
            if not (n.small and n.id in visited):
                paths += count_paths_from(n, visited + [n.id])
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
print(count_paths_from(nodes['start'], visited = ['start']))

