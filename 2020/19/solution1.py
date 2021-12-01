def expand(rule):
    """
    input: a rule of the form [['123', '124'], ['124', '123']]
     if 123 = [['456', '457'], ['457', '456']]
     if 124 = [['789', '780'], ['780', '789']]
    then output: a rule of the form [['456', '457', '789', '780'], ['456', '457', '780', '789'], ['457', '456', '789', '780'], ['457', '456', '780', '789']
                        , ['789', '780', '456', '457'], ['780', '789', '456', '457'], ['789', '780', '457', '456'], ['780', '789', '457', '456']]
    """
    out = []
    changed = False
    for option in rule:
        print('option', option)
        new = []
        for num in option:
            if num in ('a', 'b'):
                new.append(num)
            else:
                changed = True
                rule = rule_dict[num]
                print('rule', num, '=', rule)
                for 
                new.extend(rule)
        out.append(new)
                # if len(option) > 1:
                #     if option[1] in ('a', 'b'):
                #         out.append(option[1])
                #     else:
                #         changed = True
                #         rule2 = rule_dict[option[1]]
                #         print('rule2', option[1], '=', rule2)
                #         for a in rule1:
                #             for b in rule2:
                #                 out.append(a+b)
                # else:
                #     for a in rule1:
                #         out.append(a)

    return out, changed





#script
data = open("input.txt", "r").read().splitlines()


rule_dict = {}
for row in data[:133]:
    num, string  = row.split(': ')
    rules  = string.split(' | ')
    rules = [x.split(' ') for x in rules]
    rule_dict[num] = rules

cont = True
new_rule_dict = {}

while cont:
    for rule in rule_dict:
        print(rule)
        if 


# permissable = [rule_dict['0']] 
# print(permissable)


# changed = True
# counter = 0
# while changed and counter < 2:
#     print('\n*********')
#     new_permissable = []
#     changed = False
#     counter += 1

#     for rule in permissable:
#         print('\nrule: ', rule)
#         new, changed = expand(rule)
#         new_permissable.append(new)
                

#     permissable = new_permissable
#     print(permissable)