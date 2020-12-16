import math

#script
data = open("input.txt", "r").read().splitlines()
ranges = {}
error_rate = 0

#extract the ranges
for x in data[:20]:

    name, rngs = x.split(': ')
    rng_1, rng_2 = rngs.split(' or ')
    lower_1, upper_1 = [int(x) for x in rng_1.split('-')]
    lower_2, upper_2 = [int(x) for x in rng_2.split('-')]

    ranges[name] = [[lower_1, upper_1],[lower_2, upper_2]]

#find valid tickets
valid_tickets = []
for row in data[25:]:
    ticket = [int(x) for x in  row.split(',')]

    for num in ticket:
        for field, rngs in ranges.items(): #look for invalid numbers
            valid = 0
            if  (num >= rngs[0][0] and num <= rngs[0][1]) or (num >= rngs[1][0] and num <= rngs[1][1]) :
                valid = 1
                break

        if valid == 0:
            break

    if valid == 1:
        valid_tickets.append(ticket)
            

#get possible positions for each field
ticket_length = len(valid_tickets[0])
possible_positions = {}

for field, rngs in ranges.items():
    possible_positions[field] = [1] * ticket_length
    for i in range(ticket_length):
        for ticket in valid_tickets:
            num = ticket[i]
            if possible_positions[field][i] == 1:
                if  (num >= rngs[0][0] and num <= rngs[0][1]) or (num >= rngs[1][0] and num <= rngs[1][1]) :
                    pass
                else:
                    possible_positions[field][i] = 0
                    break

#find the correct position for each field
position_index = {}
cont = True
while cont:
    cont = False
    for field, p in possible_positions.items():
        if sum(p) == 1:
            cont = True
            idx = p.index(1)
            position_index[field] = idx
            for field2, p2 in possible_positions.items(): 
                possible_positions[field2][idx] = 0


#extract answer from your ticket
answers = []
your_ticket = ticket = [int(x) for x in  data[22].split(',')]

for field, p in position_index.items():
    if 'departure' in field:
        answers.append(your_ticket[p])


print(math.prod(answers))
        



