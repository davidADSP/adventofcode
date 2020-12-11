import csv
import copy

#script
data = [list(x) for x in open("input.txt", "r").read().splitlines()]
changed = True
rounds = 0
height = len(data)
width = len(data[0])

def count_occupied_in_view(i, j):
    occupied = 0 
    for x in range(-1,2):
        for y in range(-1,2):
            counter = 1
            if not (x==0 and y==0):
                while 0<=i+x*counter<height and 0<=j+y*counter<width:
                    seat = data[i+x*counter][j+y*counter]
                    if seat == '#':
                        occupied += 1
                        break
                    elif seat == 'L':
                        break
                    else:
                        counter += 1

    return occupied

while changed:
    new_data = copy.deepcopy(data)
    rounds += 1
    occupied_seats = 0
    changed = False

    for i, row in enumerate(data):
        for j, seat in enumerate(row):
            if seat == 'L':
                if count_occupied_in_view(i,j) == 0:
                    new_data[i][j] = '#'
                    changed = True
            if seat == '#':
                occupied_seats += 1
                if count_occupied_in_view(i,j) >= 5:
                    new_data[i][j] = 'L'
                    changed = True

    data = copy.deepcopy(new_data)

    # with open(f"./out_{rounds}.csv","w") as f:
    #     wr = csv.writer(f)
    #     wr.writerows(data)

print(occupied_seats)
                


