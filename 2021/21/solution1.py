positions = [int(x.split(':')[1]) for x in open("input.txt", "r").read().splitlines()]

scores = [0,0]
turn = 0
target = 1000
dice_num = 1
spaces = 10
rolls = 0

while True:
    rolls += 3
    move = 3 * dice_num + 3
    positions[turn] = ((positions[turn] + move - 1) % spaces) + 1
    scores[turn] += positions[turn]
    if scores[turn] >= target:
        loser = 1 - turn
        answer = scores[loser] * rolls
        break
    turn = (turn + 1) % 2
    dice_num += 3
    
print('scores', scores)
print('positions', positions)
print('dice', dice_num)
print('rolls', rolls)
print('answer', answer)


