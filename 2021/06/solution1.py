from collections import Counter

data = [int(x) for x in open("input.txt", "r").read().splitlines()[0].split(',')]
days = 80
counts = Counter(data)

for i in range(days):
    zeros = counts[0]
    for key in range(8):
        counts[key] = counts[key + 1]
    counts[6] += zeros
    counts[8] = zeros

print(sum(counts.values()))