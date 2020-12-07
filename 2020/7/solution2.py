#imports
import re

#funcs
def n_inside(suitcase):
    total = 0
    for colour, count in bags[suitcase].items():
        total += count * (1 + n_inside(colour))
    return total

#script
data = open("input.txt", "r").read().splitlines()
bags = {}
total = 0
for row in data:
    suitcase, contents = row.split(' contain')
    suitcase = re.search(r'(.+) bags', suitcase).group(1)
    contents = contents.split(', ')
    
    #create 'bags' as a dict of dicts e.g. bags = {'shiny gold': {'dull pink': 3, ... }, ...}
    if ' no other bags.' in contents:
        bags[suitcase] = {}
    else:
        regex = lambda x: re.search(r'(\d*) ?(.+) bags?', x.strip())
        bags[suitcase] = dict([(regex(x).group(2), int(regex(x).group(1))) for x in contents])

print(n_inside('shiny gold'))