#script
data = open("input.txt", "r").read().splitlines()
answers = ''
total = 0
for row in data:
    if row == '':
        total += len(set(answers))
        answers = ''
    else:
        answers = answers + row

total += len(set(answers))
print(total)