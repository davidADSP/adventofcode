import numpy as np

class Cell():
    def __init__(self, value):
        self.value = int(value)
        self.marked = False

    def mark(self):
        self.marked = True

    def __repr__(self):
        return str(self.value)

data = np.array([list(map(Cell, x)) for x in open("input.txt", "r").read().splitlines()])
cells = np.pad(data, 1, constant_values = Cell(9))

todo = set()
basins = []

for i in range(1, cells.shape[0] - 1):
    for j in range(1, cells.shape[1] - 1):
        cell = cells[i,j]
        if not cell.marked and cell.value < 9:
            basin = []
            todo.add((cell, i, j))
            while len(todo) > 0:
                basin_cell, x, y = todo.pop()
                basin_cell.mark()
                basin.append(basin_cell)
                for a,b in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
                    neighbour = cells[a,b]
                    if neighbour.value < 9 and not neighbour.marked:
                        todo.add((neighbour, a, b))
            basins.append(basin)

sizes = sorted([len(x) for x in basins])
print(np.prod(sizes[-3:]))




