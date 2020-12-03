

x = open("input.txt", "r").readline()
# x = '1,9,10,3,2,3,11,0,99,30,40,50'

data = [int(y) for y in x.split(",")]

data[1] = 12
data[2] = 2


cont = True

pos = 0

while cont:
    
    if data[pos] == 1:
        n1 = data[data[pos+1]]
        n2 = data[data[pos+2]]
        ans = n1+n2
        data[data[pos+3]] = ans
        

        pos += 4

    elif data[pos] == 2:
        n1 = data[data[pos+1]]
        n2 = data[data[pos+2]]
        ans = n1*n2
        data[data[pos+3]] = ans

        pos += 4

    elif data[pos] == 99:
        cont = False

    



print(data)