import numpy as np
data = [list(x) for x in open("input.txt", "r").read().splitlines()]

lookup = {')':1, ']': 2, '}': 3   , '>': 4}
answer = 0
scores = []

for row in data:
    closing = []
    corrupt = False
    for x in row:
        if x == '(':
            closing.append(')')
        elif x == '[':
            closing.append(']')
        elif x == '{':
            closing.append('}')
        elif x == '<':
            closing.append('>')
        elif x != closing.pop():
            corrupt = True
            break

    if not corrupt:
        score = 0
        for c in reversed(closing):
            score *= 5
            score += lookup[c]
        scores.append(score)

print(int(np.median(scores)))
