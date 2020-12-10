#script
data = [int(x) for x in open("input.txt", "r").read().splitlines()]
data.sort()
device_jolt = max(data) + 3
data.append(device_jolt)

paths = {x:0 for x in range(-3,device_jolt+1)}
paths[0] = 1
for jolt in data:
    paths[jolt] = paths[jolt-3] + paths[jolt-2] + paths[jolt-1]

print(paths[device_jolt])