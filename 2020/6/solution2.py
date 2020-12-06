from collections import Counter

#script
data = open("input.txt", "r").read().splitlines()
answers = ''
people = 0
total = 0

for row in data:
    if row == '':
        counts = Counter(answers)
        total += sum(value == people for value in counts.values())

        answers = ''
        people = 0
    else:
        people += 1
        answers = answers + row

total += sum(value == people for value in counts.values())
print(total)
    