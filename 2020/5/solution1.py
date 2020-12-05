#script
data = open("input.txt", "r").read().splitlines()
seats = []
for x in data:
    row = int('0b' + ''.join(['0' if l == 'F' else '1' for l in x[:7]]), 2)
    col = int('0b' + ''.join(['0' if l == 'L' else '1' for l in x[7:]]), 2)

    seats.append(8 * row + col)

print(max(seats))