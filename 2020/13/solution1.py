#script
data = open("input.txt", "r").read().splitlines()
time = int(data[0])
buses = [int(x) for x in data[1].split(',') if x != 'x']
best_bus = None
best_wait = None

for bus in buses:
    wait = (((time // bus) + 1) * bus) - time
    if best_wait is None or wait < best_wait:
        best_wait = wait
        best_bus = bus

print(best_wait * best_bus)    