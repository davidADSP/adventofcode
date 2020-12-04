import re

#params
total = 0
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


#functions
def check_complete(ppt_dct):
    return all(field in ppt_dct for field in required_fields)

def check_byr(x):
    return 1920 <= int(x) <= 2002

def check_iyr(x):
    return 2010 <= int(x) <= 2020

def check_eyr(x):
    return 2020 <= int(x) <= 2030

def check_hgt(x):
    cm = re.findall(r'(\d+)cm', x)
    inch = re.findall(r'(\d+)in', x)
    if cm:
        return 150 <= int(cm[0]) <= 193
    elif inch:
        return 59 <= int(inch[0]) <= 76
    else:
        return False

def check_hcl(x):
    return bool(re.search(r'^#(?:[0-9a-f]{6})$', x))

def check_ecl(x):
    return x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def check_pid(x):
    return bool(re.search(r'^(?:[0-9]{9})$', x))
       
def check_valid(passport):
    ppt_dct = dict([tuple(x.split(':')) for x in passport.split()])
    complete = check_complete(ppt_dct)
    if complete:
        byr = check_byr(ppt_dct['byr'])
        iyr = check_iyr(ppt_dct['iyr'])
        eyr = check_eyr(ppt_dct['eyr'])
        hgt = check_hgt(ppt_dct['hgt'])
        hcl = check_hcl(ppt_dct['hcl'])
        ecl = check_ecl(ppt_dct['ecl'])
        pid = check_pid(ppt_dct['pid'])

        valid = byr and iyr and eyr and hgt and hcl and ecl and pid
    else:
        valid = False

    return valid

#script
data = open("input.txt", "r").read().splitlines()
passport = ''

for row in data:
    if row != '':
        passport += ' ' + row
    else:
        total += check_valid(passport)
        passport = ''
     
total += check_valid(passport)
print(total)


