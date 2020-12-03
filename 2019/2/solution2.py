

x = open("input.txt", "r").readline()
# x = '1,9,10,3,2,3,11,0,99,30,40,50'

master_data = [int(y) for y in x.split(",")]



for i in range(100):

    for j in range(100):
        data = master_data.copy()

        data[1] = i
        data[2] = j

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

            
        if data[0] == 19690720:
            print('solution')
            print(i)
            print(j)
            print(100*i + j)
            break

