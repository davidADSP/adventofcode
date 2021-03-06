from collections import deque

#script
data = open("input.txt", "r").read().splitlines()
data = [int(x) for x in data[0].split(',')]

mem = {}
n = 0

for x in data:
    n += 1
    mem[x] = deque([n], maxlen = 2)

while n < 30000000:
    n += 1

    if len(mem[x]) == 1:
        x = 0
    else:
        x = mem[x][1] - mem[x][0]

    if x not in mem:
        mem[x] = deque([n], maxlen = 2)
    else:
        mem[x].append(n)

print(x)