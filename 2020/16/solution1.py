from pprint import pprint
#script
data = open("input.txt", "r").read().splitlines()
ranges = {}
error_rate = 0

for x in data[:20]:

    name, rngs = x.split(': ')
    rng_1, rng_2 = rngs.split(' or ')
    lower_1, upper_1 = [int(x) for x in rng_1.split('-')]
    lower_2, upper_2 = [int(x) for x in rng_2.split('-')]

    ranges[name] = [[lower_1, upper_1],[lower_2, upper_2]]

for row in data[26:]:
    nums = [int(x) for x in  row.split(',')]

    
    for num in nums:
        for field, rngs in ranges.items():
            valid = 0
            if  (num >= rngs[0][0] and num <= rngs[0][1]) or (num >= rngs[1][0] and num <= rngs[1][1]) :
                valid = 1
                break

        if valid == 0:
            error_rate += num
            
print(error_rate)
