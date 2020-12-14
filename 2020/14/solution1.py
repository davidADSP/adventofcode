import re

memory = {}

#script
data = open("input.txt", "r").read().splitlines()

for row in data:
    if row[:4] == 'mask':
        mask = row[7:]
    else:
        mem = re.search(r'mem\[(.*)\]', row).group(1)
        val = int(re.search(r'\= (.*)', row).group(1))

        binary = bin(val)[2:].zfill(36)

        new_binary = ''
        for b ,m in zip(binary, mask):
            new_binary += m if m != 'X' else b
                
        new_val = int(new_binary, 2)
        
        memory[mem] = new_val

print(sum(memory.values()))