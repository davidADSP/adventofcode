import numpy as np
from dijkstar import Graph, find_path

## expand the grid
cells = np.array([list(x) for x in open("input.txt", "r").read().splitlines()], dtype = int)

## build the graph
size = len(cells)
g = Graph()

for i in range(size):
    for j in range(size):      
        if i>0:
            g.add_edge((i-1,j), (i,j), cells[i,j])
        if i<size-1:
            g.add_edge((i+1,j), (i,j), cells[i,j])
        if j>0:
            g.add_edge((i,j-1), (i,j), cells[i,j])
        if j<size-1:
            g.add_edge((i,j+1), (i,j), cells[i,j])

g.add_edge((size-1,size-1), 'end', 1)

answer = find_path(g, (0,0), 'end')
print(answer.total_cost - 1)