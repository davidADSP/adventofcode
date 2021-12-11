import numpy as np
cells = np.array([list(x) for x in open("input.txt", "r").read().splitlines()], dtype = int)
steps = 0

while len(np.unique(cells)) > 1:
    cont = True
    cells += 1
    steps += 1
    while cont:
        cont = False
        flashes = 0
        for i in range(cells.shape[0]):
            for j in range(cells.shape[1]):
                if cells[i,j] >= 10:
                    flashes += 1
                    cells[i,j] = 0
                    for a in range(-1,2):
                        for b in range(-1,2):
                            if (i+a >= 0) and (i+a < cells.shape[0]) and (j+b >= 0) and (j+b < cells.shape[1]):
                                if cells [i+a,j+b] > 0:
                                    cells[i+a,j+b] += 1               
        if flashes > 0:
            cont = True
    
print(steps)