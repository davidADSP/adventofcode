#script
data = open("input.txt", "r").read().splitlines()
seats = [int('0b' + ''.join(['0' if l in ('F', 'L') else '1' for l in x]), 2) for x in data]
print(max(seats))