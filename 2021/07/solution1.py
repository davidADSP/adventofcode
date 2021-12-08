import numpy as np
data = [int(x) for x in open("input.txt", "r").read().splitlines()[0].split(',')]
av = int(np.median(data))
fuel = sum([abs(x - av) for x in data])
print(fuel)
