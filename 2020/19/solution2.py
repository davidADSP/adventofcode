import re

#funcs

def do_brackets(row):
    print(row)
    matches = True
    while matches:
        for symbol in symbol_order:
            matches = re.findall(rf'(\d+\{symbol}\d+)', row)
            if matches:
                x = matches[0]
                row = row.replace(x, str(eval(x)), 1)
                break
    print('=', row)
    return row

#script
data = open("input.txt", "r").read().splitlines()
ans = []
symbol_order = ['+', '*']

for row in data:
    row = row.replace(' ', '')
    start_row = ''
    while row != start_row:
        print(row)
        start_row = row
        matches = re.findall(r'\(([\d\+\*]+)\)', row)
        for x in matches:
            row = row.replace(x, str(do_brackets(x)), 1)
            break

        row = re.sub(r'\((\d+)\)', r'\1', row)

    row = do_brackets(row)
    ans.append(int(row))
    print(row)
    print()
            
print(sum(ans))


        
        
        
        



    

