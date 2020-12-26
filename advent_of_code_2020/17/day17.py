# https://adventofcode.com/2020/day/17
# 3d conway of life
from collections import defaultdict
f = open('input.txt', 'r')
lines = f.read().strip().split('\n')

x = 0
y = 0
z = 0
q = 0
sp = defaultdict(int)
for line in lines:
    x = 0
    for c in line:
        if c == '#':
            sp[(x, y, z, q)] = 1
        x += 1
    y += 1

print sp
for i in xrange(6):
    toCheck = set()
    for (x,y,z,q), v in sp.iteritems():
        for i in xrange(-1, 2):
            for j in xrange(-1, 2):
                for k in xrange(-1, 2):
                    for w in xrange(-1, 2):
                        toCheck.add((x + i, y+j, z + k, q+w))
    active = 0
    n = defaultdict(int)
    for (x,y,z,q) in toCheck:
        v = sp[(x,y,z,q)]
        alive = 0
        for i in xrange(-1, 2):
            for j in xrange(-1, 2):
                for k in xrange(-1, 2):
                    for w in xrange(-1, 2):
                        if not (i == 0 and j == 0 and k == 0 and w == 0):
                             alive += sp[(x + i, y+j, z + k, q + w)]
        changed = False
        if v:
            if (alive == 2 or alive == 3):
                n[(x,y,z, q)] = 1
                changed = True
        elif v == 0 and alive == 3:
            n[(x,y,z,q)] = 1
            changed = True
        if changed:
            active += 1
    sp = n
    print active

