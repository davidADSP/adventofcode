import re
import copy
import numpy as np
from pprint import pprint

costs = {
'A': 1
,'B': 10
, 'C': 100
, 'D': 1000
}

mapping = {
2: 'A'
, 4: 'B'
, 6: 'C'
, 8: 'D'
}

mapping_inv = {
'A': 2
,'B': 4
,'C': 6
,'D': 8
}

hash_table = {}

def try_move(i,j, cells, letter): # from i to j

    if i < j: #i is to the left of the j
        for k in range(i+1,j+1):
            if cells[k] != '':
                return None
    else:
        for k in range(i-1,j-1, -1):
            if cells[k] != '':
                return None
    
    return (abs(i-j)) * costs[letter]

def get_possible_moves(cols, cells):
    moves = []
    # moving from cells to cols
    for j, cell in cells.items():
        if cell != '':
            i = mapping_inv[cell]
            col = cols[i]
            if sum([x != cell for x in col]) == 0:
                col_energy = (col_depth - len(col)) * costs[cell]  # to get to top of column
                energy = try_move(j, i, cells, cell)
                if energy is not None:
                    # print(i,j,energy)
                    new_cols = copy.deepcopy(cols)
                    new_cells = copy.deepcopy(cells)
                    new_cols[i].append(cell)
                    new_cells[j] = ''
                    moves.append((col_energy + energy, new_cols, new_cells))


    if len(moves) == 0:
        # moving from cols to cells
        for i, col in cols.items():
            if len(col)>0 and sum([x != mapping[i] for x in col]) > 0 :
                letter = col[-1]
                col_energy = (col_depth + 1 - len(col)) * costs[letter] # to get to top of column
                for j in (0,1,3,5,7,9,10):
                    energy = try_move(i, j, cells, letter)
                    if energy is not None:
                        new_cols = copy.deepcopy(cols)
                        new_cells = copy.deepcopy(cells)
                        letter = new_cols[i].pop()
                        new_cells[j] = letter
                        moves.append((col_energy + energy, new_cols, new_cells))

    return moves


def solved(cols):
    for i, letter in mapping.items():
        if not cols[i] == [letter] * col_depth:
            return False
    return True

def calc_min_energy(cols, cells):

    if (str(cols), str(cells)) in hash_table:
        return hash_table[(str(cols), str(cells))][0]

    if solved(cols):
        return 0

    moves = get_possible_moves(cols, cells) # moves = (energy, new_cols, new_cells)
    
    if len(moves) > 0:
        energy = min([e + calc_min_energy(new_cols, new_cells) for e, new_cols, new_cells in moves])
        chosen = moves[np.argmin([e + calc_min_energy(new_cols, new_cells) for e, new_cols, new_cells in moves])]
        hash_table[(str(cols), str(cells))] = (energy, chosen)
        return energy
    else:
        hash_table[(str(cols), str(cells))] = (1e10, None)
        return 1e10

data = [x for x in open("input.txt", "r").read().splitlines()]

rows = [[x[3], x[5], x[7], x[9]] for x in data[2:4]]
cols = {i: x[::-1] for i, x in zip((2,4,6,8), list(map(list, zip(*rows))))}
cells = {i: '' for i in range(11)}

col_depth = len(cols[2])

answer = calc_min_energy(cols, cells)

while True:
    h = hash_table[(str(cols), str(cells))]
    cols = h[1][1]
    cells = h[1][2]
    print('********')
    print(cols)
    print(cells)

    if h[0] == h[1][0]:
        break

print(answer)
