numbers = []
answer = 0
for x in open("input.txt", "r"):
    numbers.append(int(x))

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i-1]:
        answer +=1

print(answer) 

