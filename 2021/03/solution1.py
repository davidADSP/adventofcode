counts_0 = [0] * 12
counts_1 = [0] * 12

data = [list(x) for x in open("input.txt", "r").read().splitlines()]

for d in data:
    for i, x in enumerate(d):
        if x == '0':
            counts_0[i] += 1
        else:
            counts_1[i] += 1

gamma_rate = ''
epsilon_rate = ''

for c0,c1 in zip(counts_0, counts_1):
    if c1 > c0:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'

print(gamma_rate)
print(epsilon_rate)

print(int(gamma_rate, 2) * int(epsilon_rate, 2) )

