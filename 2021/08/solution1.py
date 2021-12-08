import numpy as np
data = [x.split(' | ') for x in open("input.txt", "r").read().splitlines()]
answer = 0
for d in data:
    signal = d[0].split(' ')
    value = d[1].split(' ')
    for v in value:
        if len(v) in (2,3,4,7):
            answer+=1
print(answer)

