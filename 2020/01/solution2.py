numbers = []
for x in open("input.txt", "r"):
    numbers.append(int(x))

for m in numbers:
    for n in numbers:
        p = 2020-m-n
        if p in numbers:
            print(m * n * p)
            break