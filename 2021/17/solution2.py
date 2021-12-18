import math

xrng, yrng = [x for x in open("input.txt", "r").read().splitlines()][0][15:].split(', y=')

xL, xR = [int(x) for x in xrng.split('..')]
yB, yT = [int(x) for x in yrng.split('..')]

a = 1
b = 1
c = -2 * xL

min_vx = math.ceil(( -b + math.sqrt(pow(b, 2) -  4 * a * c) ) / (2 * a))
max_vx = xR
min_vy = yB
max_vy = -yB-1

max_t = 2 * max_vy + 2

count = 0

for vx in range(min_vx, max_vx + 1):
    for vy in range(min_vy, max_vy + 1):
        for t in range(1, max_t+1):
            if t<=vx:
                x = t * vx - t * (t-1) // 2
            else:
                x = vx * (vx + 1) // 2
            
            y = t * vy - t * (t-1) // 2

            if x >= xL and x <= xR and y>= yB and y<=yT:
                count += 1 
                break
            
            if x > xR or y < yB:
                break

print(count)

