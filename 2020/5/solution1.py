#script
data = open("input.txt", "r").read().splitlines()
seats = []
for x in data:
    seat = int('0b' + ''.join(['0' if l in ('F', 'L') else '1' for l in x]), 2)
    seats.append(seat)

print(max(seats))