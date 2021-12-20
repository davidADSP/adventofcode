import numpy as np

iterations = 50

data = [list(x) for x in open("input.txt", "r").read().splitlines()]
enhancement = data[0]
grid = np.array(data[2:])

for i in range(1, iterations + 1):
    print(i)
    reference = grid.copy()
    new_grid = np.full_like(grid, '.')

    if i == 1:
        new_grid = np.pad(new_grid, 2, constant_values = '.')
        reference = np.pad(reference, 2, constant_values = '.')
    elif i % 2 == 0:
        new_grid = np.pad(new_grid, 2, constant_values = enhancement[0])
        reference = np.pad(reference, 2, constant_values = enhancement[0])
    else:
        new_grid = np.pad(new_grid, 2, constant_values = enhancement[-1])
        reference = np.pad(reference, 2, constant_values = enhancement[-1])

    for row in range(1, new_grid.shape[0] - 1):
        for col in range(1, new_grid.shape[1] - 1):

            square = reference[(row-1):(row+2),(col-1):(col+2)]
            num = int(''.join(np.where(square.flatten() == '#', '1', '0')),2)
            new_grid[row,col] = enhancement[num]

    new_grid = new_grid[1:new_grid.shape[0] - 1, 1:new_grid.shape[1] - 1 ]
    grid = new_grid

print((grid == '#').sum())


