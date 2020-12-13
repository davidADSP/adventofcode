import math

forest = open("input.txt", "r").read().splitlines()
n_rows = len(forest)
n_cols = len(forest[0])

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
totals = []

for right, down in slopes:
    hits = 0
    i = 0
    row = 0
    col = 0
    while True:
        i += 1
        row, col = i * down, (i * right) % n_cols

        if row < n_rows:
            tree = int(forest[row][col] == '#')
            hits += tree
        else:
            break
    
    totals.append(hits)

print(totals)
print(math.prod(totals))