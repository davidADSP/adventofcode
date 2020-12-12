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

def shift(p, waypoint, distance):
    p = [x+y*distance for x,y in zip(position, waypoint)]
    return p

def rotate(waypoint, direction, distance):
    if direction == 'R':
        if distance == 90:
            waypoint = [-waypoint[1], waypoint[0]]
        if distance == 180:
            waypoint = [-waypoint[0], -waypoint[1]]
        if distance == 270:
            waypoint = [waypoint[1], -waypoint[0]]
    if direction == 'L':
        if distance == 90:
            waypoint = [waypoint[1], -waypoint[0]]
        if distance == 180:
            waypoint = [-waypoint[0], -waypoint[1]]
        if distance == 270:
            waypoint = [-waypoint[1], waypoint[0]]
    return waypoint


#script
data = open("input.txt", "r").read().splitlines()
position = [0,0]
waypoint = [1,10]

for row in data:
    direction = row[0]
    distance = int(row[1:])

    if direction in ('N','S','E','W'):
        waypoint = translate(waypoint, direction, distance)
    elif direction in ('L', 'R'):
        waypoint = rotate(waypoint, direction, distance)
    elif direction == 'F':
        position = shift(position, waypoint, distance)

print(sum([abs(x) for x in position]))

    