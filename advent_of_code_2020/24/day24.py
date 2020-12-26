# https://adventofcode.com/2020/day/24
# hexgrid conway's game of life. Learned from somewhere the trick is to assign different weights to the directions.
from collections import defaultdict
import copy
import math

D = {
        'e': (0, 2),
        'w': (0, -2),
        'se': (1, 1),
        'sw': (1, -1),
        'nw': (-1, -1),
        'ne': (-1, 1),
        }

def get_directions(line):
    ret = []
    i = 0
    while i < len(line):
        if line[i] in ['e', 'w']:
            ret.append(D[line[i]])
            i += 1
        elif line[i:i+2] in 'se,sw,nw,ne'.split(','):
            ret.append(D[line[i:i+2]])
            i += 2
        else:
            print 'error parsing'
    return ret

f = open('input.txt', 'r')
times = defaultdict(int)
for line in f.read().strip().split('\n'):
    dirs = get_directions(line)
    start = (0, 0)
    for d in dirs:
        start = (start[0] + d[0], start[1] + d[1])
    times[start] += 1

tiles = defaultdict(int)
for c, v in times.iteritems():
    if v % 2:
        tiles[c] = 1

for i in xrange(100):
    neighbors = defaultdict(int)
    n = defaultdict(int)
    for t, v in tiles.iteritems():
        if not v:
            continue
        for d, tup in D.iteritems():
            neighbors[(t[0] + tup[0], t[1] + tup[1])] += 1
    for t, v in tiles.iteritems():
        if v and not (neighbors[t] == 0 or neighbors[t] > 2):
                n[t] = 1
    for t, v in neighbors.iteritems():
        if tiles[t] == 0 and v == 2:
            n[t] = 1
    tiles = n


print len(tiles)
