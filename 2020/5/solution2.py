#script
data = open("input.txt", "r").read().splitlines()
seats = []
for x in data:
    row = int('0b' + ''.join(['0' if l == 'F' else '1' for l in x[:7]]), 2)
    col = int('0b' + ''.join(['0' if l == 'L' else '1' for l in x[7:]]), 2)

    seats.append(8 * row + col)

seats.sort()
current_seat = seats[0]
for seat in seats:
    if seat != current_seat:
        print(current_seat)
        break
    current_seat+=1
    