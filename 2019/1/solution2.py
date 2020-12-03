
total_fuel = 0

def fuel_calc(mass):
    return int(mass / 3) - 2

for x in open("input.txt", "r"):
    mass = float(x)
    cont = True
    while cont:
        fuel = fuel_calc(mass)
        if fuel > 0:
            total_fuel += fuel
            mass = fuel
            print(fuel, total_fuel)
        else:
            cont = False

print(total_fuel)