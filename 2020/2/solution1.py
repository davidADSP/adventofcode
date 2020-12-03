total = 0
for x in open("input.txt", "r"):
    rng, letter, pwd = x.split()
    lower, upper = [int(x) for x in rng.split('-')]
    letter = letter[0]

    cnt = pwd.count(letter)

    if cnt >= lower and cnt <= upper:
        total += 1

print(total)