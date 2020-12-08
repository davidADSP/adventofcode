#funcs

def check(data):
    idx = 0
    acc = 0
    terminate = False
    visited = {}

    while True:
        if idx in visited:
            break

        if idx == len(data):
            terminate = True
            break
        
        visited[idx] = True
        command, val = data[idx].split(' ')
        val = int(val)

        if command == 'acc':
            acc += val
            idx += 1
        elif command == 'jmp':
            idx += val
        elif command == 'nop':
            idx += 1

    return acc, terminate


def edit_data(data, idx, new_line):
    data[idx] = new_line
    return data

#script
data = open("input.txt", "r").read().splitlines()

for idx, row in enumerate(data):
    command, val = row.split(' ')
    if command in ('jmp', 'nop'):
        new_word = 'nop' if command == 'jmp' else 'jmp'
        new_data = edit_data(data.copy(), idx, f'{new_word} {val}')
        acc, terminate = check(new_data)

        if terminate:
            print(acc)
            break
        

    

