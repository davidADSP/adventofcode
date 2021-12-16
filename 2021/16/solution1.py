import numpy as np

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


def parse_operator(m):
    length_type = bits[m]
    m += 1
    versions = []
    if length_type == '0':
        length = int(bits[m:m+15],2)
        m += 15
        print(f'Length + = {length}')
        i = m
        while m-i < length:
            v, m = parse_packet(m)
            versions += v
    else:
        length = int(bits[m:m+11],2)
        m += 11
        print(f'Length x = {length}')
        for i in range(length):
            v, m = parse_packet(m)
            versions += v
    return versions, m


def parse_packet(m):
    version = int(bits[m:m+3],2)
    m += 3
    type_id = int(bits[m:m+3],2)
    m += 3
    print(f'\nVersion = {version}')
    print(f'Type ID = {type_id}')
    versions = [version]
    if type_id == 4:
        literal, m = parse_literal(m)
    else:
        v, m = parse_operator(m)
        versions += v
    return versions, m



string = [x for x in open("input.txt", "r").read().splitlines()][0]
bits = ''.join([lookup[s] for s in string])
m = 0
version_sum = 0
versions = []
while int(bits[m:],2) > 0:
    print(f'\n\nm = {m}/{len(bits)}')
    v, m = parse_packet(m)
    versions.extend(v)

print(f'\nVersion Sum = {sum(versions)}')




