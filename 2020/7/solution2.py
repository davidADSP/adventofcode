#imports
import re

#funcs
def n_inside(suitcase):
    counts = []
    for colour, count in bags[suitcase].items():
        counts.append(count * (1 + n_inside(colour)))
    return sum(counts)

#script
data = open("input.txt", "r").read().splitlines()
bags = {}
total = 0
for row in data:
    bag, contains_str = row.split(' contain')
    bag = re.search(r'(.+) bags', bag).group(1)

    contains = contains_str.split(', ')
    
    #create 'bags' as a dict of dicts e.g. bags = {'shiny gold': {'dull pink': 3, ... }, ...}
    if ' no other bags.' in contains:
        bags[bag] = {}
    else:
        regex = re.search(r'(\d*) ?(.+) bags?', x.strip())
        count_bags = [int(regex.group(1)) for x in contains]
        hold_bags = [regex.group(2) for x in contains]
        bags[bag] = dict(zip(hold_bags, count_bags))

print(n_inside('shiny gold'))