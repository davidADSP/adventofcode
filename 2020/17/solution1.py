from pprint import pprint

#funcs

def count_active(coords, grid):
    n = 0
    a, b, c = coords
    for i in range(-1,2):
        for j in range(-1,2):
            for k in range(-1,2):
                if not (i==0 and j==0 and k ==0):
                    if (a+i, b+j, c+k) in grid:
                        if grid[(a+i, b+j, c+k)] == '#':
                            n+=1           
    return n

#script
data = open("input.txt", "r").read().splitlines()
ROUNDS = 6
SIZE = len(data)

grid = {}

for a in range(-ROUNDS, ROUNDS + SIZE):
    for b in range(-ROUNDS, ROUNDS + SIZE):
        for c in range(-ROUNDS, ROUNDS + SIZE):
            coord = (a,b,c)
            grid[coord] = '.'

for r, row in enumerate(data):
    for c, col in enumerate(row):
        coord = (r,c,0)
        grid[coord] = col



for rnd in range(ROUNDS):
    # print(grid)
    new_grid = {}
    for coords, val in grid.items():
        n = count_active(coords, grid)
        if val == '#':
            if n in (2,3):
                new_grid[coords] = '#'
            else:
                new_grid[coords] = '.'
        else:
            if n == 3:
                new_grid[coords] = '#'
            else:
                new_grid[coords] = '.'
    
    grid = new_grid.copy()

    
    
    # print(new_grid)
    # print()

answer = 0
for coords, val in grid.items():
    if val == '#':
        answer += 1

print(answer)