import re

data = [x for x in open("input.txt", "r").read().splitlines()]
pattern = r"(\w+) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)"

switches = []
x = []
y = []
z = []
pos = {}

for d in data:
    switch, x1, x2, y1, y2, z1, z2 = re.match(pattern, d).groups()

    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    z1 = int(z1)
    z2 = int(z2)

    switches.append(switch)
    x.append((x1,x2))
    y.append((y1,y2))
    z.append((z1,z2))

    if -50<=x1<=50 and -50<=x2<=50 and -50<=y1<=50 and -50<=y2<=50 and -50<=z1<=50 and -50<=z2<=50:
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                for k in range(z1, z2+1):
                    pos[(i,j,k)] = switch

answer = list(pos.values()).count('on')
print(answer)