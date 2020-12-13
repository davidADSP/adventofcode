import numpy as np

#script
data = open("input.txt", "r").read().splitlines()
time = int(data[0])
buses = [int(x) for x in data[1].split(',') if x != 'x']
remainders = [-i for i, x in enumerate(data[1].split(',')) if x != 'x']

n = 0
bigM = np.prod(buses)

for m, a in zip(buses, remainders):
    # Chinese Remainder Theorem 
    # This bad boy is the smallest solution to a system of r modular equations x = a mod(m) where the m's are coprime
    # n = a1M1y1 + a2M2y2 + · · · + arMryr   mod(bigM)
    M = int(bigM // m)
    y = pow(M % m, -1, m)
    n += a * M * y
   
print(n % bigM)



    
