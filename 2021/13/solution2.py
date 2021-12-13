import numpy as np
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

for f in folds:
    for p in points:
        if f['direction'] == 'x':
            direction = 0
        else:
            direction = 1

        if p[direction] > f['location']:
            p[direction] = f['location'] - (p[direction] - f['location'])

    points = [list(x) for x in set(tuple(x) for x in points)]

x = [x[0] for x in points]
y = [x[1] for x in points]

arr = np.zeros((max(y)+1,max(x)+1))
arr[y, x] = 1

for x in arr:
    print(''.join(['▨' if y == 0 else ' '  for y in x]))


            

