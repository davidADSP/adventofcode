#script
data = open("input.txt", "r").read().splitlines()
idx = 0
acc = 0
visited = {}
while True:
    if idx in visited:
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

print(acc)