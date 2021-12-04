import numpy as np
from classes import Cell, Line, Board

def parse_data(data):
    iterator = iter(data)
    numbers = [int(x) for x in next(iterator).split(',')]
    boards = []
    board_num = 0  
    while next(iterator, None) is not None:
        rows = []
        for i in range(5):
            rows.append([Cell(int(x)) for x in next(iterator).split(' ') if x!=''])
        rows = np.array(rows)
        cols= rows.T
        lines = [Line(x) for x in rows.tolist() + cols.tolist()]
        boards.append(Board(lines))
    
    return numbers, boards