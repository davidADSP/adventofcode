import numpy as np
data = np.array([list(x) for x in open("input.txt", "r").read().splitlines()], dtype = int)
cells = np.pad(data, 1, constant_values = 10)
answer = 0
for i in range(1, cells.shape[0] - 1):
    for j in range(1, cells.shape[1] - 1):
        if cells[i,j] < cells[i+1,j] \
            and cells[i,j] < cells[i-1,j] \
            and cells[i,j] < cells[i,j+1] \
            and cells[i,j] < cells[i,j-1]:
        
            answer += cells[i,j] + 1

print(answer)