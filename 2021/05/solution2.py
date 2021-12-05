from funcs import parse_row

data = open("input.txt", "r").read().splitlines()
coords = {}

for row in data:

    hits = parse_row(row, all_lines = True)
    for h in hits:
        if h in coords:
            coords[h] += 1
        else:
            coords[h] = 1

answer = 0
for h,v in coords.items():
    if v > 1:
        answer += 1

print(answer)
