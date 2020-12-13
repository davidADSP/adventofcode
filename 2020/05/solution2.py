#script
data = open("input.txt", "r").read().splitlines()
seats = [int('0b' + ''.join(['0' if l in ('F', 'L') else '1' for l in x]), 2) for x in data]
seats.sort()

current_seat = seats[0]
for seat in seats:
    if seat != current_seat:
        print(current_seat)
        break
    current_seat+=1
    