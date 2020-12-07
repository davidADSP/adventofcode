#script
import re

data = open("input.txt", "r").read().splitlines()
bags = {}
total = 0
for row in data:
    bag, holds = row.split(' contain')
    bag = re.search(r'(.+) bags', bag).group(1)
    hold_bags = [re.search(r'(\d*) ?(.+) bags?', x.strip()).group(2) for x in holds.split(', ')]
    bags[bag] = hold_bags

gold_bags = ['shiny gold']
for colour in gold_bags:
    for bag, hold_bags in bags.items():
        if colour in hold_bags:
            gold_bags.append(bag) if bag not in gold_bags else None

print(len(gold_bags) - 1)