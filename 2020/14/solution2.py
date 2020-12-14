import re
# funcs


def expand(floating_binary):
    binaries = [floating_binary]
    for binary in binaries:
        new_binary = list(binary)
        for i, bit in enumerate(binary):
            if bit == 'X':
                new_binary[i] = '0'
                binaries.append(''.join(new_binary))
                new_binary[i] = '1'
                binaries.append(''.join(new_binary))
                break

    binaries = [x for x in binaries if 'X' not in x]

    return binaries

#script
memory = {}
data = open("input.txt", "r").read().splitlines()

for row in data:
    if row[:4] == 'mask':
        mask = row[7:]
    else:
        mem = int(re.search(r'mem\[(.*)\]', row).group(1))
        val = int(re.search(r'\= (.*)', row).group(1))

        binary = bin(mem)[2:].zfill(36)

        floating_binary = ''
        for b ,m in zip(binary, mask):
            floating_binary += '1' if m == '1' else b if m == '0' else 'X'

        mem_locations = expand(floating_binary)

        for mem in mem_locations:
            memory[int(mem, 2)] = val


print(sum(memory.values()))