from collections import Counter

wires = []

grids = [[],[]]
wire_num = 0

for x in open("input.txt", "r"):

    wire_list = x.split(",")

    wire = []
    current_pos = [0,0]

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

            
            grids[wire_num].append(tuple(current_pos))

    

    grids[wire_num] = set(grids[wire_num])

    wire_num += 1


print(type(grids[0])) 
print(grids[1])     

result = {element for element in grids[0] if element in grids[1]}


closest = None
closest_dist = 1e10

for r in result:
    dist = abs(r[0]) + abs(r[1])
    if dist<closest_dist:
        closest_dist = dist
        closest = r

# print(result)
# print(closest)
# print(closest_dist)


