current_right = 0
total = 0
row = 0

forest = open("input.txt", "r").read().splitlines()

for x in forest:
    if row == 0:
        pass
    else:
        tree = int(x[current_right] == '#')
        total += tree

    current_right = (current_right + 3) % len(x)
    row += 1

print(total)