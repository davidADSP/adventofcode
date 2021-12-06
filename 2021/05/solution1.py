from funcs import parse_row
from collections import Counter

data = open("input.txt", "r").read().splitlines()
coords = Counter()

for row in data:
    hits = parse_row(row, include_diagonals = False)
    coords.update(hits)
        
answer = sum(v > 1 for v in coords.values())
print(answer)
