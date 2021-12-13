# Get data
data = [x for x in open("input.txt", "r").read().splitlines()]
folds = []
points = []

for d in data:
    if 'fold along' in d:
        direction, location = d.split('=')
        direction = direction[-1]
        location = int(location)
        folds.append({'direction': direction, 'location': location})
    elif ',' in d:
        x, y = [int(x) for x in d.split(',')]
        points.append([x,y])

for f in folds[:1]:
    for p in points:
        if f['direction'] == 'x':
            direction = 0
        else:
            direction = 1

        if p[direction] > f['location']:
            p[direction] = f['location'] - (p[direction] - f['location'])

    points = [list(x) for x in set(tuple(x) for x in points)]

print(len(points))

            

