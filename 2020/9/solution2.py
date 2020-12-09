#script
data = [int(x) for x in open("input.txt", "r").read().splitlines()]
INVALID = 69316178
start = 0
end = 1
cont = True

while cont:
    rng = data[start:(end+1)]
    while sum(rng) < INVALID:
        end+=1 
        rng = data[start:(end+1)]
        if sum(rng) == INVALID:
            print(min(rng) + max(rng))
            cont = False
            break
    start += 1
    end = start + 1
    
