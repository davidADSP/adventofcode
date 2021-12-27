import numpy as np

grid = np.array([list(x) for x in open("input.txt", "r").read().splitlines()])

step = 0
mode = 0
changes = 0
i_lim, j_lim = grid.shape


while True:

    if mode == 1:
        step += 1

    new_grid = np.full_like(grid, '.')
    
    for i in range(i_lim):
        for j in range(j_lim):
            
            if mode == 0:
                if grid[i,j] == '>':
                    if j == j_lim - 1:
                        j_lookup = 0
                    else:
                        j_lookup = j + 1

                    if grid[i, j_lookup] == '.':
                        new_grid[i, j_lookup] = '>'
                        changes += 1
                    else:
                        new_grid[i, j] = '>'
                elif grid[i,j] == 'v':
                    new_grid[i, j] = grid[i,j]
                
            else:
                if grid[i,j] == 'v':
                    if i == i_lim - 1:
                        i_lookup = 0
                    else:
                        i_lookup = i + 1
                    # print((i_lookup, j))
                    if grid[i_lookup, j] == '.':
                        new_grid[i_lookup, j] = 'v'
                        # print(new_grid)
                        changes += 1
                    else:
                        new_grid[i, j] = 'v'
                elif grid[i,j] == '>':
                    new_grid[i, j] = grid[i,j]


    grid = new_grid.copy()

    if changes == 0 and mode == 1:
        break

    if mode == 1:
        changes = 0

    mode = 1 - mode


print('answer', step)


