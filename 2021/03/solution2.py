

data = [x for x in open("input.txt", "r").read().splitlines()]
data = sorted(data)

## oxygen

oxygen = ''
oxygen_data = data.copy()
l = len(oxygen_data)
bit = 0

while l > 1:
    if l % 2 == 0:
        x1 = oxygen_data[l // 2][bit]
        x2 = oxygen_data[l // 2 - 1][bit]
        if x1 == x2:
            oxygen += x1
        else:
            oxygen += '1'
    else:
        oxygen += oxygen_data[(l - 1) // 2][bit]

    oxygen_data = [x for x in oxygen_data if x.startswith(oxygen)]

    l = len(oxygen_data)
    bit += 1


oxygen_answer = oxygen_data[0]


## co2
co2 = ''
co2_data = data.copy()
l = len(co2_data)
bit = 0

while l > 1:
    if l % 2 == 0:
        x1 = co2_data[l // 2][bit]
        x2 = co2_data[l // 2 - 1][bit]
        if x1 == x2:
            co2 += str(1-int(x1))
        else:
            co2 += '0'
    else:
        x1 = co2_data[(l - 1) // 2][bit]
        co2 += str(1-int(x1))

    co2_data = [x for x in co2_data if x.startswith(co2)]

    l = len(co2_data)
    bit += 1

co2_answer = co2_data[0]


print(oxygen_answer)
print(co2_answer)
print(int(oxygen_answer,2) * int(co2_answer,2))
