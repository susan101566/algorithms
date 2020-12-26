# https://adventofcode.com/2020/day/5
# each line in the input encodes a seat on a plane according to some binary definition, e.g. f/b is front/back. Find the seat that's missing.
f = open('input.txt', 'r')
lines = f.read().strip().splitlines()

ids = {}
maxrow = 0

def calc(row):
    rge = [0, 128]
    for c in row[:-3]:
        r = (rge[1] - rge[0])/2
        if c == 'F':
            rge = [rge[0], rge[0] + r]
        if c == 'B':
            rge = [rge[0] + r, rge[1]]
    r1 = rge[0]
    global maxrow
    maxrow = max(maxrow, r1)
    rge = [0, 8]
    for c in row[-3:]:
        r = (rge[1] - rge[0])/2
        if c == 'L':
            rge = [rge[0], rge[0] + r]
        if c == 'R':
            rge = [rge[0] + r, rge[1]]
    r2 = rge[0]
    return r1 * 8 + r2

score = 0
for line in lines:
    score = calc(line)
    ids[score] = True

for i in xrange(128):
    for j in xrange(8):
        sc = i * 8 + j
        if sc not in ids and sc - 1 in ids and sc + 1 in ids:
            print i, j
            print i * 8 + j

