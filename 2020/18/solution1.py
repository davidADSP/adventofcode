from pprint import pprint

#funcs

def update_solution(sol, operation, val):
    if operation == '+':
        sol+=val
    elif operation == '*':
        sol*=val
    
    return sol

def solve_brackets(string):

    sol = 0
    bracket_count = 0
    inner_string = ''
    operation = '+'

    for i, s in enumerate(string):
        print(s)
        # print('Brackets:', bracket_count)
        
        if bracket_count > 0:
            
            if s == ')':
                bracket_count -= 1

                if bracket_count == 0:
                    print(inner_string)
                    val = solve_brackets(inner_string)
                    sol = update_solution(sol, operation, val)
                    inner_string = ''
                    print('Sol', sol) 
                else:
                    inner_string += s
            elif s == '(':
                bracket_count += 1
                inner_string += s
            else:
                inner_string += s

        else:
            
            if s == ' ':
                pass
            elif s in ('+', '*'):
                operation = s
            elif s == '(':
                bracket_count += 1
            else:
                val = int(s)
                sol = update_solution(sol, operation, val)
                print('Sol', sol)


    return sol


            
    

#script
data = open("input.txt", "r").read().splitlines()


ans = []
for row in data:
    ans.append(solve_brackets(row))


print(sum(ans))