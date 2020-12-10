#script
data = [int(x) for x in open("input.txt", "r").read().splitlines()]
data.sort()
device_jolt = max(data) + 3
data.append(device_jolt)
diffs = {1:0, 2:0, 3:0}
previous_jolt = 0

for jolt in data:
    diffs[jolt - previous_jolt] += 1
    previous_jolt = jolt

print(diffs[1] * diffs[3])