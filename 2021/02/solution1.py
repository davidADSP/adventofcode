forward = 0
depth = 0

data = [x.split(' ') for x in open("input.txt", "r").read().splitlines()]

for direction, amount in data:
    amount = int(amount)
    if direction == 'forward':
        forward += amount
    elif direction == 'up':
        depth -= amount
    elif direction == 'down':
        depth += amount

print(forward * depth) 

