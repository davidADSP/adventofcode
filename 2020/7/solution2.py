#script
import re

data = open("input.txt", "r").read().splitlines()
bags = {}
total = 0
for row in data:
    bag, contains_str = row.split(' contain')
    bag = re.search(r'(.+) bags', bag).group(1)

    contains = contains_str.split(', ')

    if ' no other bags.' in contains:
        bags[bag] = {}
    else:
        count_bags = [int(re.search(r'(\d*) ?(.+) bags?', x.strip()).group(1)) for x in contains]
        hold_bags = [re.search(r'(\d*) ?(.+) bags?', x.strip()).group(2) for x in contains]
        bags[bag] = dict(zip(hold_bags, count_bags))

def n_inside(suitcase):
    counts = []
    for colour, count in bags[suitcase].items():
        counts.append(count * (1 + n_inside(colour)))
    return sum(counts)

print(n_inside('shiny gold'))