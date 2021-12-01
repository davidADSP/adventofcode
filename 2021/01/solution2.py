numbers = []
answer = 0
for x in open("input.txt", "r"):
    numbers.append(int(x))

for i in range(1, len(numbers)-2):
    a = sum(numbers[i:i+3])
    b = sum(numbers[i-1:i+2])
    if  a > b:
        answer +=1

print(answer) 
