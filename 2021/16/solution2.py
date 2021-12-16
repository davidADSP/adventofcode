import numpy as np
import math

lookup = {
    '0': '0000'
    ,'1': '0001'
    ,'2': '0010'
    ,'3': '0011'
    ,'4': '0100'
    ,'5': '0101'
    ,'6': '0110'
    ,'7': '0111'
    ,'8': '1000'
    ,'9': '1001'
    ,'A': '1010'
    ,'B': '1011'
    ,'C': '1100'
    ,'D': '1101'
    ,'E': '1110'
    ,'F': '1111'
}

def handle(values, type_id):
    if type_id == 0: #sum
        return sum(values)
    elif type_id == 1: #product
        return math.prod(values)
    elif type_id == 2: #minimum
        return min(values)
    elif type_id == 3: #maximum
        return max(values)
    elif type_id == 5: # >
        return int(values[0] > values[1])
    elif type_id == 6: # <
        return int(values[0] < values[1])
    else: # =
        return int(values[0] == values[1])


def parse_literal(m):
    leader = bits[m]
    m += 1
    literal = ''
    while leader == '1':
        literal += bits[m:m+4]
        m += 4
        leader = bits[m]
        m += 1
    
    literal += bits[m:m+4]
    m += 4

    literal = int(literal, 2)

    print(f'Literal = {literal}')

    return literal, m


def parse_operator(m, type_id):
    length_type = bits[m]
    m += 1
    values = []
    if length_type == '0':
        
        length = int(bits[m:m+15],2)
        m += 15
        print(f'Length + = {length}')

        i = m
        while m-i < length:
            v, m = parse_packet(m)
            values.append(v)

    else:
        length = int(bits[m:m+11],2)
        m += 11
        print(f'Length x = {length}')
        for i in range(length):
            v, m = parse_packet(m)
            values.append(v)

    value = handle(values, type_id)

    return value, m


def parse_packet(m):
    version = int(bits[m:m+3],2)
    m += 3
    type_id = int(bits[m:m+3],2)
    m += 3

    print(f'Type ID = {type_id}')

    if type_id == 4:
        return parse_literal(m)
    else:
        return parse_operator(m, type_id)


string = [x for x in open("input.txt", "r").read().splitlines()][0]
bits = ''.join([lookup[s] for s in string])
m = 0
value, _ = parse_packet(m)

print(f'\nValue = {value}')




