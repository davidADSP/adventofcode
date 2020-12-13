total = 0
for x in open("input.txt", "r"):
    rng, letter, pwd = x.split()
    lower, upper = [int(x) for x in rng.split('-')]
    letter = letter[0]

    first_check = pwd[lower - 1] == letter
    second_check = pwd[upper - 1] == letter

    if (first_check and not second_check) or (second_check and not first_check):
        total += 1

print(total)