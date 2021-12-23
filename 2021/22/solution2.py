import re

data = [x for x in open("input.txt", "r").read().splitlines()]
pattern = r"(\w+) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)"

cuboids = []

def get_cuboid(d):
    switch, x1, x2, y1, y2, z1, z2 = re.match(pattern, d).groups()
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    z1 = int(z1)
    z2 = int(z2)
    return (switch, x1, x2, y1, y2, z1, z2)

def get_overlap(a1,a2,b1,b2):    

    if a2<b1:
        return (a1,a2, 0), (b1, b2, 1)
    elif a1<b1 and a2>=b1 and a2<b2:
        return (a1, b1-1, 0), (b1, a2, 2), (a2+1, b2, 1)
    elif a1<b1 and a2>b2:
        return (a1, b1-1, 0), (b1, b2, 2), (b2+1, a2, 0)
    elif a1>b1 and a2<b2:
        return (b1, a1-1, 1),  (a1, a2, 2), (a2+1, b2, 1)
    elif a1>b1 and a1<=b2 and a2>b2:
        return (b1, a1-1, 1), (a1, b2, 2), (b2+1, a2, 0)
    elif a1>b2:
        return (b1, b2, 1), (a1, a2, 0)
    elif a1==b1 and a2<b2:
        return  (a1, a2, 2), (a2+1, b2, 1)
    elif a1==b1 and a2>b2:
        return (a1, b2, 2), (b2+1, a2, 0)
    elif a1==b1 and a2==b2:
        return ((a1, a2, 2),)
    elif a2==b2 and a1<b1:
        return  (a1, b1-1, 0), (b1, a2, 2)
    elif a2==b2 and a1>b1:
        return (b1, a1-1, 1), (a1, a2, 2)
    else:
        print(a1,a2,b1,b2)
        exit()


def calc_overlap(a,b):
    new_cuboids = []
    (aswitch, ax1, ax2, ay1, ay2, az1, az2) = a
    (bswitch, bx1, bx2, by1, by2, bz1, bz2) = b

    overlaps = []
    for pairs in (ax1, ax2, bx1, bx2), (ay1, ay2, by1, by2), (az1, az2, bz1, bz2):
        overlaps.append(get_overlap(*pairs))

    for i in overlaps[0]:
        x1,x2,xtype = i
        if xtype != 1:
            for j in overlaps[1]:
                y1,y2,ytype = j
                if ytype != 1:
                    for k in overlaps[2]:
                        z1,z2,ztype = k
                        if ztype != 1:
                            checks = [xtype, ytype, ztype]
                            if 0 in checks:
                                new_cuboids.append(('on', x1,x2,y1,y2,z1,z2))
                
    return new_cuboids

counter = 0
for d in data:
    counter+=1
    print(counter)
    print(len(cuboids))
    next_cuboid = get_cuboid(d)
    new_cuboids = []

    for c in cuboids:
        out = calc_overlap(c, next_cuboid)
        new_cuboids.extend(out)
        
    if next_cuboid[0] == 'on':
        new_cuboids.append(next_cuboid)

    cuboids = new_cuboids
   
area = 0
for c in cuboids:
    area += (c[2] - c[1] + 1) * (c[4] - c[3] + 1) * (c[6] - c[5] + 1)

print(area)