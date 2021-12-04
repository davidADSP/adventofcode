import numpy as np
from funcs import parse_data

data = open("input.txt", "r").read().splitlines()
numbers, boards = parse_data(data)

for num in numbers:
    for board in boards:
        board.update(num)
        if board.complete():
            answer = board.unmarked_sum() * num
            print(answer)
            exit()