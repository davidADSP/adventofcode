import numpy as np
from funcs import parse_data

data = open("input.txt", "r").read().splitlines()
numbers, boards = parse_data(data)

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