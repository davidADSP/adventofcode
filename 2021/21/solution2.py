positions = [int(x.split(':')[1]) for x in open("input.txt", "r").read().splitlines()]
target = 21
spaces = 10

dice_rolls = {
    3:1
    ,4:3
    ,5:6
    ,6:7
    ,7:6
    ,8:3
    ,9:1
}

def calc_wins(wins, scores, positions, turn):
    if scores[0] >= target:
        out = [wins[0] + 1, wins[1]]
        return out

    if scores[1] >= target:
        out = [wins[0], wins[1] + 1]
        return out

    new_pos = [((positions[turn] + m - 1) % spaces) + 1 for m in dice_rolls]
    new_score = [scores[turn] + p for p in new_pos]

    if turn == 0:
        w = [calc_wins(wins, [s, scores[1]], [p, positions[1]], 1-turn) for p,s in zip(new_pos, new_score)]
    else:
        w = [calc_wins(wins, [scores[0], s], [positions[0], p], 1-turn) for p,s in zip(new_pos, new_score)]
    out = [[y[0] * d, y[1] * d] for y, d in zip(w, dice_rolls.values())]
    out = [sum(i) for i in zip(*out)]
    return out

wins = calc_wins([0,0], [0,0], positions, 0)
print(max(wins))