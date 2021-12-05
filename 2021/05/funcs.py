import numpy as np

def parse_row(row, all_lines):
    hits = []
    c1, c2 = row.split(' -> ')
    x1,y1 = [int(x) for x in c1.split(',')]
    x2,y2 = [int(x) for x in c2.split(',')]

    if all_lines or (x1 == x2 or y1 == y2):

        x_direction = np.sign(x2-x1)
        y_direction = np.sign(y2-y1)

        l = max(abs(x2-x1), abs(y2-y1)) + 1

        for i in range(l):
            hits.append((x1 + i * x_direction, y1 + i * y_direction))
    
    return hits


    