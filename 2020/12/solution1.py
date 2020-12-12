directions = ['N', 'E', 'S', 'W']

# funcs:
def translate(p, direction, distance):
    if direction == 'N':
        p[0] += distance
    elif direction == 'S':
        p[0] -= distance
    elif direction == 'E':
        p[1] += distance
    elif direction == 'W':
        p[1] -= distance
    return p

def turn(facing, direction, distance):
    hops = distance // 90
    current_pos = directions.index(facing)
    if direction == 'R':
        new_pos =  (current_pos + hops ) % 4
    if direction == 'L':
        new_pos =  (current_pos - hops ) % 4

    return directions[new_pos]

#script
data = open("input.txt", "r").read().splitlines()
facing = 'E'
position = [0,0]
for row in data:
    direction = row[0]
    distance = int(row[1:])

    if direction in ('N','S','E','W'):
        position = translate(position, direction, distance)
    
    elif direction in ('L', 'R'):
        facing = turn(facing, direction, distance)
    elif direction == 'F':
        position = translate(position, facing, distance)

print(sum([abs(x) for x in position]))

    