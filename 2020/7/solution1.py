#script
import re

data = open("input.txt", "r").read().splitlines()
bags = {}
total = 0
for row in data:
    suitcase, contents = row.split(' contain')
    suitcase = re.search(r'(.+) bags', suitcase).group(1)
    contents = [re.search(r'(\d*) ?(.+) bags?', x.strip()).group(2) for x in contents.split(', ')]
    bags[suitcase] = contents

gold_bags = ['shiny gold']
for colour in gold_bags:
    for suitcase, contents in bags.items():
        if colour in contents:
            gold_bags.append(suitcase) if suitcase not in gold_bags else None

print(len(gold_bags) - 1) # don't count the shiny gold bag itself