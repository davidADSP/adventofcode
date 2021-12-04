import numpy as np
from classes import Cell, Line, Board

#Create the boards
data = open("input.txt", "r").read().splitlines()
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

#Play Bingo
answer = None
complete_boards = 0
for num in numbers:
    for board in boards:
        if not board.done:
            board.update(num)
            if board.complete():
                complete_boards += 1
                board.done = True
                if complete_boards == len(boards):
                    answer = board.unmarked_sum() * num
                    print(answer)
                    exit()