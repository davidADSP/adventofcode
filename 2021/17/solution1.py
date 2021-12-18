xrng, yrng = [x for x in open("input.txt", "r").read().splitlines()][0][16:].split(', y=')

xL, xR = [int(x) for x in xrng.split('..')]
yB, yt = [int(x) for x in yrng.split('..')]

answer = (-yB) * (-yB - 1) // 2
print(answer)