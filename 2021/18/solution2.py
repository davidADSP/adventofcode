import re
import math

values = []
data = [x for x in open("input.txt", "r").read().splitlines()]
counter = 1

for i in range(len(data)):
    for j in range(len(data)):
        string = '[' + data[i] + ',' + data[j] + ']'
        m = 0
        depth = 0
        pair = ''
        number = ''
        mode = 'e'
        while m < len(string) or mode == 'e':
            # print(f'Found {string[m]} @ depth {depth}\tpair {pair}   \tnum {number}')
            if string[m] == '[':
                depth += 1
                m += 1
                pair = ''
                number = ''
                pair_start = ''
                num_start = ''
            elif string[m] == ']':
                number = ''
                if len(pair) > 0 and depth >= 5 and mode == 'e':
                    # EXPLODE !
                    pair_list = [int(x) for x in pair.split(',')]
                    # print(f'Exploding pair {pair_list} @ depth {depth}')
                    next_num = r"\d+" # find the first next number
                    match = re.search(next_num, string[m:])
                    if match:
                        start = match.start() + m
                        end = match.end() + m
                        num = str(int(match.group()) + pair_list[1])
                        string = string[:start] + num + string[end:]
                    previous_num = r"(\d+)(?!.*\d)" # find the last previous number
                    match = re.search(previous_num, string[:pair_start])
                    if match:
                        start = match.start()
                        end = match.end()
                        num = str(int(match.group()) + pair_list[0])
                        string = string[:start] + num + string[end:]
                        # adjustment if the string has shifted due to the insertion
                        m += len(num) - len(str(int(match.group())))
                        pair_start += len(num) - len(str(int(match.group())))
                    string = string[:pair_start-1] + '0' + string[m+1:]
                    # print(f'After Explode: {string}\n')
                    m = 0
                    depth = 0
                    # input()
                else:
                    depth -= 1
                    m += 1
                    pair = ''
                    num = ''
            elif string[m].isnumeric():
                if number == '':
                    num_start = m
                    if pair == '':
                        pair_start = m
                    number = string[m]
                    pair += string[m]
                    m += 1
                else:
                    number += string[m]
                    pair += string[m]

                    if string[m+1].isnumeric(): #number continues
                        m += 1
                    else:
                        if mode == 's':
                            # SPLITTING!
                            # print(f'Split number {number}')
                            number_int = int(number)
                            lower = str(math.floor(number_int / 2))
                            upper = str(math.ceil(number_int / 2))
                            string = string[:num_start] + '[' + lower + ',' + upper + ']' + string[m+1:]
                            # print(f'After Splitting: {string}\n')
                            m = 0
                            depth = 0
                            mode = 'e'
                            # input()
                        else:
                            m += 1
            elif string[m] == ',':
                pair += string[m]
                m += 1
                number = ''
            if m>=len(string) and mode == 'e':
                mode = 's'
                m = 0

        print(f'OUTPUT {counter}: {string}')
        counter+=1

        def calc_value(pair):
            if type(pair[0]) == list and type(pair[1]) == list:
                out = 3 * calc_value(pair[0]) + 2 * calc_value(pair[1])
            elif type(pair[0]) == list:
                out = 3 * calc_value(pair[0]) + 2 * pair[1]
            elif type(pair[1]) == list:
                out = 3 * pair[0] + 2 * calc_value(pair[1])
            else:
                out = 3 * pair[0] + 2 * pair[1]
            return out

        answer = eval(string)
        values.append(calc_value(answer))
        
print(max(values))




