import numpy as np
from collections import Counter

r = []
r.append(lambda x,y,z:  np.array([x,y,z]))
r.append(lambda x,y,z:  np.array([x,-z,y]))
r.append(lambda x,y,z:  np.array([x,-y,-z]))
r.append(lambda x,y,z:  np.array([x,z,-y]))
r.append(lambda x,y,z:  np.array([-x,y,-z]))
r.append(lambda x,y,z:  np.array([-x,-z,-y]))
r.append(lambda x,y,z:  np.array([-x,-y,z]))
r.append(lambda x,y,z:  np.array([-x,z,y]))

r.append(lambda y,z,x:  np.array([x,y,z]))
r.append(lambda y,z,x:  np.array([x,-z,y]))
r.append(lambda y,z,x:  np.array([x,-y,-z]))
r.append(lambda y,z,x:  np.array([x,z,-y]))
r.append(lambda y,z,x:  np.array([-x,y,-z]))
r.append(lambda y,z,x:  np.array([-x,-z,-y]))
r.append(lambda y,z,x:  np.array([-x,-y,z]))
r.append(lambda y,z,x:  np.array([-x,z,y]))

r.append(lambda z,x,y:  np.array([x,y,z]))
r.append(lambda z,x,y:  np.array([x,-z,y]))
r.append(lambda z,x,y:  np.array([x,-y,-z]))
r.append(lambda z,x,y:  np.array([x,z,-y]))
r.append(lambda z,x,y:  np.array([-x,y,-z]))
r.append(lambda z,x,y:  np.array([-x,-z,-y]))
r.append(lambda z,x,y:  np.array([-x,-y,z]))
r.append(lambda z,x,y:  np.array([-x,z,y]))

data = [x for x in open("input.txt", "r").read().splitlines()]
scanners = []

for d in data:
    if 'scanner' in d:
        beacons = []
    if ',' in d:
        beacons.append([int(x) for x in d.split(',')])
    if len(d) == 0:
        scanners.append(beacons)

scanners.append(beacons)

signal_id = 0
signal_pos = [0,0,0]
beacons = set()
signals = {}
threshold = 12

signals[signal_id] = signal_pos
beacons.update([tuple(x) for x in scanners[0]])

print('# Beacons = ', len(beacons))

while len(signals) < len(scanners):
    for signal_id, reference in enumerate(scanners):
        if signal_id in signals:
            print(f'\nReference sensor {signal_id}')
            dist1 = np.array([[np.abs(np.subtract(x,y)).sum() for x in reference] for y in reference])
            for i, s in enumerate(scanners):
                if i not in signals and i != signal_id:
                    # print(f'Checking sensor {i}')
                    dist2 = np.array([[np.abs(np.subtract(x,y)).sum() for x in s] for y in s])
                    overlaps = []
                    for n1, row1 in enumerate(dist1):
                        for n2, row2 in enumerate(dist2):
                            o = list((Counter(row1) & Counter(row2)).elements())
                            if len(o) >= threshold:
                                overlaps.append((n1, n2, len(o)))
                                break
                    if len(overlaps) >= threshold:
                        originals = [reference[x[0]] for x in overlaps]
                        for rot in r:
                            trans = [rot(*s[x[1]]) for x in overlaps]
                            diff = [tuple(x-y) for x,y in zip(originals, trans)]
                            if len(set(diff)) == 1:
                                print(f'Found a pair {signal_id} - {i}')
                                signal_pos = list(diff[0])
                                signals[i] = signal_pos
                                print(f'Signal {i} pos {signal_pos}')
                                scanners[i] = [list(signal_pos + rot(*x)) for x in s]
                                beacons.update([tuple(x) for x in scanners[i]])
                                print('# Beacons = ', len(beacons))
                                break
print('\n')
print('# joined signals = ', len(signals))
print('# Beacons = ', len(beacons))

max_dist = 0
for signal1 in signals.values():
    for signal2 in signals.values():
        max_dist = max(max_dist, sum([abs(x-y) for x,y in zip(signal1, signal2)]))

print('Max Dist = ', max_dist)
                    
