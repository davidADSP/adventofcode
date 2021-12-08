import numpy as np

def get_fuel(data, pos):
    distance = [abs(x - pos) for x in data]
    fuel = sum([x  * (x+1) // 2  for x in distance])
    return fuel

data = [int(x) for x in open("input.txt", "r").read().splitlines()[0].split(',')]
av = np.mean(data)
pos1, pos2 = int(np.floor(av)), int(np.ceil(av))
fuel1, fuel2 = get_fuel(data, pos1), get_fuel(data, pos2)
print(min(fuel1, fuel2))