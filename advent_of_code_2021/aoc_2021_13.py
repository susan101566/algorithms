from collections import defaultdict
f = open('input.txt', 'r')

def fold(coords, axis, v):
    i = 0 if axis == 'x' else 1
    newcoords = set()
    for coord in coords:
        if coord[i] < v:
            newcoords.add(coord)
        else:
            nt = [0, 0]
            nt[1-i] = coord[1-i]
            nt[i] = v - (coord[i] - v)
            newcoords.add(tuple(nt))
    return newcoords

part2 = False
coords = set() 
foldings = []
for line in f.read().strip().split('\n'):
    if line.strip() == '':
        part2 = True
        continue
    if not part2:
        x, y = map(int, line.split(','))
        coords.add((x, y))
    else:
        p1, p2 = line.split('=')
        foldings.append((p1[-1], int(p2)))

for (a, v) in foldings:
    coords = fold(coords, a, v)

arr = [[' ' for _ in xrange(50)] for _ in xrange(50)]
for (x, y) in coords:
    arr[y][x] = '#'

for l in arr:
    print ''.join(l)
