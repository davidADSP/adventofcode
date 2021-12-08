import numpy as np
from collections import Counter

data = [x.split(' | ') for x in open("input.txt", "r").read().splitlines()]

nums = {
    (0,1,2,4,5,6): '0'
    , (2,5): '1'
    , (0,2,3,4,6) : '2'
    , (0,2,3,5,6) : '3'
    , (1,2,3,5): '4'
    , (0,1,3,5,6): '5'
    , (0,1,3,4,5,6): '6'
    , (0,2,5): '7'
    , (0,1,2,3,4,5,6): '8'
    , (0,1,2,3,5,6): '9'
}

answer = 0

for d in data:

    signals = d[0].split(' ')
    values = d[1].split(' ')

    freq = Counter(''.join(signals))

    lookup = {}

    # -- 0 --
    #|       |
    #1       2
    #|       |
    # -- 3 --
    #|       |
    #4       5
    #|       |
    # -- 6 --

    lookup[next(filter(lambda k: freq[k]==6, freq.keys()))] = 1
    lookup[next(filter(lambda k: freq[k]==4, freq.keys()))] = 4
    lookup[next(filter(lambda k: freq[k]==9, freq.keys()))] = 5
    
    one = list(next(filter(lambda x: len(x)==2, signals)))
    topandtopright = set(filter(lambda k: freq[k]==8, freq.keys()))
    lookup[list(topandtopright - set(one))[0]] = 0
    lookup[list(set(one).intersection(topandtopright))[0]] = 2

    four = list(next(filter(lambda x: len(x)==4, signals)))
    middleandmiddlebotton = set(filter(lambda k: freq[k]==7, freq.keys()))
    lookup[list(middleandmiddlebotton - set(four))[0]] = 6
    lookup[list(set(four).intersection(middleandmiddlebotton))[0]] = 3

    answer += int(''.join([nums[tuple(sorted([lookup[letter] for letter in v]))] for v in values]))

print(answer)