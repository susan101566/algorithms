import re
from collections import defaultdict

def printer(field, y1, y2, x1, x2):
    for y in xrange(y1, y2+1):
        print ''.join(field[y][x1: x2+1])

f = open('input.txt', 'r')
lines = f.read().strip().split('\n')
field = [['.' for x in xrange(2500)] for _ in xrange(2500)]
field[0][500] = '+'
miny = 2500
maxy = 0
for line in lines:
    r = re.match(r'(?P<p1>.)=(?P<p2>.*), (?P<p3>.)=(?P<p4>.*)\.\.(?P<p5>.*)', line)
    v1k = r.group('p1')
    v1v = int(r.group('p2'))
    v2 = r.group('p3')
    r1 = int(r.group('p4'))
    r2 = int(r.group('p5'))
    if v1k == 'x':
        for i in xrange(r1, r2+1):
            field[i][v1v] = '#'
        miny = min(miny, r1)
        maxy = max(maxy, r2)
    else:
        for i in xrange(r1, r2+1):
            field[v1v][i] = '#'
        miny = min(miny, v1v)
        maxy = max(maxy, v1v)

watery = 0
waterx = 500
def find_range(field, y, x, is_rock):
    base_range = None
    left = -1
    right = 2500
    allowed = ['#'] if is_rock else ['.', '~', '|']
    for i in xrange(x, -1, -1):
        if field[y][i] not in allowed:
            left = i+1
            break
    for i in xrange(x, 2500):
        if field[y][i] not in allowed:
            right = i-1
            break
    return (left, right)

def drip(field, watery, waterx):
    global maxy
    base_range = None
    starty = watery
    # find base
    while True:
        if starty > maxy:
            break
        c = field[starty][waterx]
        # found base
        if c == '#':
            base_range = find_range(field, starty, waterx, True)
            break
        if field[starty][waterx] == '.':
            field[starty][waterx] = '|'
        starty += 1
    # fill water
    overleft = None
    overright = None
    overy = None
    if base_range == None and watery <= maxy:
        for i in xrange(watery, maxy+1):
            if field[i][waterx] == '.':
                field[i][waterx] = '|'
        return (overleft, overright, overy)
    for y in xrange(starty-1, -1, -1):
        waters = find_range(field, y, waterx, False)
        # unbound, aka overflow
        if waters[0] <= base_range[0] or waters[1] >= base_range[1]:
            overleft = base_range[0] - 1 if waters[0] <= base_range[0] else None
            overright = base_range[1] + 1 if waters[1] >= base_range[1] else None
            overy = y
            for i in xrange(max(base_range[0], waters[0]), min(base_range[1], waters[1])+1):
                if field[y][i] == '.':
                    field[y][i] = '|'
            break
        for i in xrange(waters[0], waters[1]+1):
            if field[y][i] == '#':
                print 'bug!!!, not . when filling water'
            field[y][i] = '~'
            # drop down
            for ii in xrange(y+1, starty):
                if field[ii][i] == '.' or field[ii][i] == '|':
                    field[ii][i] = '~'
                else:
                    break
    return (overleft, overright, overy)

starts = [(0, 500)]
seen = set()
while len(starts) > 0:
    #print '================'
    #print 'queue: ', starts
    y, x = starts.pop(0)
    if (y, x) in seen:
        continue
    seen.add((y, x))
    overleft, overright, overy = drip(field, y, x)
    if overleft != None and overy != None:
        starts.append([overy, overleft])
    if overright != None and overy != None:
        starts.append([overy, overright])
    #printer(field, max(0, y-25), min(y+25, maxy), max(x-25, 0), min(x+25, 2500))
#printer(field, 0, 2500-1, 0, 2500-1)

vcount = 0
tcount = 0
for y in xrange(miny, maxy+1):
    for x in xrange(0, 2500):
        c = field[y][x]
        if c == '~': 
            tcount += 1
        if c == '|':
            vcount += 1
print vcount, tcount, vcount+tcount

