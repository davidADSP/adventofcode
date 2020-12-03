from collections import Counter

wires = []

grids = [[],[]]
wire_num = 0

for x in open("input.txt", "r"):

    wire_list = x.split(",")

    wire = []
    current_pos = [0,0]
    counter = 0
    poss = []

    for inst in wire_list:
        direction = inst[0]
        distance = int(inst[1:])

        for d in range(distance):
            
            if direction == 'U':
                current_pos[1] += 1
            elif direction == 'D':
                current_pos[1] -= 1
            elif direction == 'L':
                current_pos[0] -= 1
            elif direction == 'R':
                current_pos[0] += 1

            counter += 1

            
            grids[wire_num].append(tuple(current_pos))
            

    wire_num += 1

poss = []


for x in range(2):
    this_grid = grids[x]
    other_grid = grids[1-x]
    counter = 0
    for pos in this_grid:
        counter+=1
        if counter % 10000 == 0:
            print(counter)

        if pos in other_grid:
            d1 = other_grid.index(pos) + 1
            d2 = this_grid.index(pos) + 1
            poss.append(d1 + d2)
            print(poss)
            



print(min(poss))