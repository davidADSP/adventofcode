import csv
import copy

#script
data = [list(x) for x in open("input.txt", "r").read().splitlines()]
changed = True
rounds = 0
height = len(data)
width = len(data[0])

def count_occupied_adjacent(i, j):
    occupied = 0
    for x in range(-1,2):
        for y in range(-1,2):
            if (not (x==0 and y==0)) and (0<=i+x<height and 0<=j+y<width):
                occupied += data[i+x][j+y] == '#'
    return occupied

while changed:
    new_data = copy.deepcopy(data)
    rounds += 1
    occupied_seats = 0
    changed = False

    for i, row in enumerate(data):
        for j, seat in enumerate(row):
            if seat == 'L':
                if count_occupied_adjacent(i,j) == 0:
                    new_data[i][j] = '#'
                    changed = True
            if seat == '#':
                occupied_seats += 1
                if count_occupied_adjacent(i,j) >= 4:
                    new_data[i][j] = 'L'
                    changed = True

    data = copy.deepcopy(new_data)

    # with open(f"./out_{rounds}.csv","w") as f:
    #     wr = csv.writer(f)
    #     wr.writerows(data)
    
print(occupied_seats)
                


