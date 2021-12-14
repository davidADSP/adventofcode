from collections import Counter

# Get data
data = [x for x in open("input.txt", "r").read().splitlines()]
steps = 40
counts = Counter()

polymer = list(data[0])
start_letter = polymer[0]
end_letter = polymer[-1]

rules = [d.split(' -> ') for d in data[2:]]
rules = {tuple(r[0]): ((r[0][0], r[1]), (r[1], r[0][1]))  for r in rules}

for i in range(len(polymer) - 1):
    pair = tuple(polymer[i:i+2])
    counts[pair] += 1

for _ in range(steps):
    new_counts = Counter()
    for pair in counts:
        new_counts[rules[pair][0]] += counts[pair]
        new_counts[rules[pair][1]] += counts[pair]

    counts = new_counts

letter_counts = Counter()

for c,v in counts.items():
    letter_counts[c[0]] += v
    letter_counts[c[1]] += v

letter_counts[start_letter] += 1
letter_counts[end_letter] += 1

for c,v in letter_counts.items():
    letter_counts[c] = v // 2

print(max(letter_counts.values()) - min(letter_counts.values()))