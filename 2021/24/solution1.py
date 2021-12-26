data = [x.split(' ') for x in open("input.txt", "r").read().splitlines()]

w_list = [3,9,9,9,9,6,9,8,7,9,9,4,2,9]
counter = 0
row_counter = 0
x = 0
y = 0
z = 0

print(f'w\tx\ty\tz\tz%26\tn1\tn2\tz%26-n2')

for i, d in enumerate(data):
    row_counter += 1
    if len(d) == 2:
        op, var = d
    else:
        op, var, val = d

    if op == 'inp':
        w = w_list[counter]
        counter += 1

    if op == 'add':
        exec(f"{var} += {val}")

    if op == 'mul':
        exec(f"{var} *= {val}")
    
    if op == 'div':
        exec(f"{var} = int({var} / {val})")

    if op == 'mod':
        exec(f"{var} %= {val}")

    if op == 'eql':
        exec(f"{var} = int({var} == {val})")

    if row_counter == 6:
        n1 = int(val)

    if row_counter == 16:
        n2 = int(val)

    try:
        if i == len(data) - 1 or data[i+1][0] == 'inp':
            print(f'{w}\t{x}\t{y}\t{z}\t{z%26}\t{n1}\t{n2}\t{z%26-n2}')
            row_counter = 0
    except:
        pass
