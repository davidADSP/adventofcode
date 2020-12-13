numbers = []
for x in open("input.txt", "r"):
    numbers.append(int(x))

for n in numbers:
    if (2020 - n) in numbers:
        print(n * (2020-n))
        break

