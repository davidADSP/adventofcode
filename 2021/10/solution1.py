
data = [list(x) for x in open("input.txt", "r").read().splitlines()]

lookup = {')':3, ']': 57, '}': 1197   , '>': 25137}
answer = 0

for row in data:
    closing = []
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
            answer += lookup[x]
            break

print(answer)
