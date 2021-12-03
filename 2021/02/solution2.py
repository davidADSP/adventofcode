forward = 0
depth = 0
aim = 0

data = [x.split(' ') for x in open("input.txt", "r").read().splitlines()]

for direction, amount in data:
    amount = int(amount)
    if direction == 'forward':
        forward += amount
        depth += aim * amount
    elif direction == 'up':
        aim -= amount
    elif direction == 'down':
        aim += amount

print(forward * depth) 
