#params
total = 0
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

#functions
def check_complete(passport):
    ppt_dct = dict([tuple(x.split(':')) for x in passport.split()])
    return all(field in ppt_dct for field in required_fields)

#script
data = open("input.txt", "r").read().splitlines()
passport = ''

for row in data:
    if row != '':
        passport += ' ' + row
    else:
        total += check_complete(passport)
        passport = ''
     
total += check_complete(passport)
print(total)