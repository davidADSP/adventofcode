#script
data = open("input.txt", "r").read().splitlines()
pointer = 0
nums = []
for x in data:
    x = int(x)
    if pointer < 25:
        nums.append(x)
    else:
        inverse_nums = [x - y for y in nums]
        check = sum([y in inverse_nums and y != x/2 for y in nums]) == 0

        if check:
            print(x)
            break

        nums.append(x)
        nums.pop(0)
    pointer+= 1
    
