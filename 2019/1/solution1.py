
total_fuel = 0

for x in open("input.txt", "r"):
    mass = float(x)
    fuel = int(mass / 3) - 2
    total_fuel += fuel

print(total_fuel)