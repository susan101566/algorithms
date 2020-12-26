# https://adventofcode.com/2020/day/20
# Puzzle tiles matching. 
# Each tile can be flipped or rotated. What's the configuration of the final puzzle? An absolute nightmare, took me 4 hours, wasn't even thinking at the end. Part 1 I only considered the edges when transforming the tiles, and you only have to find the corners. Part 2 you have to do all tiles. It's exactly as it sounds, just try everything. Credits to stackoverflow for rotation.
from collections import defaultdict
import copy
import math

f = open('input.txt', 'r')
sections = f.read().strip().split('\n\n')

puzzle = {}
tiles = {}
edges = defaultdict(set)
tiledim = None
dim = int(math.sqrt(len(sections)))

def rotations(top, right, bottom, left):
    result = []
    result.append([top, right, bottom, left])
    for i in xrange(3):
        t, r, b, l = result[-1]
        result.append([l[::-1], t, r[::-1], b])
    return result

def flip(top, right, bottom, left):
    return [top[::-1], left, bottom[::-1], right]

def rot_tile(l):
    return [list(reversed(x)) for x in zip(*l)]

def flip_tile(tile, o, r):
    result = copy.deepcopy(tile)
    td = len(tile)
    if o:
        for i in xrange(td):
            for j in xrange(td):
                result[i][j] = tile[i][td-1-j]
    for i in xrange(r):
        result = rot_tile(result)
    return result

for section in sections:
    lines = section.split('\n')
    tileId = int(lines[0].split()[1][:-1])
    grid = lines[1:]
    tiles[tileId] = [list(l) for l in grid]
    tiledim = len(grid)
    top = grid[0]
    bottom = grid[-1]
    left = []
    right = []
    for line in grid:
        left.append(line[0])
        right.append(line[-1])
    hashes = [[], []]
    left = tuple(left)
    right = tuple(right)
    top = tuple(top)
    bottom = tuple(bottom)
    for v in rotations(top, right, bottom, left):
        hashes[0].append(v)
    f = flip(top, right, bottom, left)
    for v in rotations(f[0], f[1], f[2], f[3]):
        hashes[1].append(v)
    puzzle[tileId] = hashes
    for e in [left, right, top, bottom]:
        edges[e].add(tileId)
        edges[e[::-1]].add(tileId)

'''
#part1
candidates = set()
for tid, hashes in puzzle.iteritems():
    for o in xrange(2):
        for es in hashes[o]:
            singles = 0
            for e in es:
                if len(edges[e]) == 1:
                    singles += 1
            if singles == 2:
                candidates.add(tid)

print candidates
print len(candidates)
print candidates
a = 1
for c in candidates:
    a *= c
print a
'''

# part 2
def find_top_left(puzzle, edges):
    for tid, hashes in puzzle.iteritems():
        for o in xrange(2):
            for (r, es) in enumerate(hashes[o]):
                singles = []
                for i, e in enumerate(es):
                    if len(edges[e]) == 1:
                        singles.append(i)
                if singles == [0, 3]:
                    # tileId, orientation, rotation
                    return (tid, o, r)
    print 'find_top_left nothing found'
    return None

def find_right(puzzle, edges, seen, left, top):
    candidate = []
    for tid, hashes in puzzle.iteritems():
        for o in xrange(2):
            for (r, es) in enumerate(hashes[o]):
                if left and es[3] != left:
                    continue
                if top and es[0] != top:
                    continue
                if tid in seen:
                    continue
                candidate.append((tid, o, r))
    return candidate

def fill(puzzle, edges, seen, result, i, j):
    if i >= dim or j >= dim:
        return False
    matches = []
    # left
    left = None
    if j != 0:
        tid, o, r = result[i][j-1]
        left = puzzle[tid][o][r][1]
    # top
    top = None
    if i != 0:
        tid, o, r = result[i-1][j]
        top = puzzle[tid][o][r][2]
    degree2s = 4 - (i == 0) - (j == 0) - (i == dim - 1) - (j == dim-1)
    candidates = find_right(puzzle, edges,seen, left, top)
    if len(candidates) == 0:
        return False
    if i == dim - 1 and j == dim - 1 and len(candidates) == 1:
        result[i][j] = candidates[0]
        seen.add(candidates[0][0])
        return True
    for candidate in candidates:
        result[i][j] = candidate
        seen.add(candidate[0])
        if j == dim -1:
            if fill(puzzle, edges, seen, result, i+1, 0):
                return True
        else:
            if fill(puzzle, edges, seen, result, i, j+1):
                return True
        seen.remove(candidate)
    return False

result = [[None for j in xrange(dim)] for i in xrange(dim)]
topleft = find_top_left(puzzle, edges) 
result[0][0] = topleft
seen = set()
seen.add(topleft[0])
fill(puzzle, edges, seen,  result, 0, 1)
final_x = 0

final = [[None for i in xrange((tiledim-2) * dim)] for j in xrange((tiledim-2) * dim)]
for i in xrange(dim):
    for j in xrange(dim):
        tid, o, r = result[i][j]
        tile = flip_tile(tiles[tid], o, r)
        for x in xrange(1, tiledim-1):
            for y in xrange(1, tiledim-1):
                final[i * (tiledim-2)+x-1][j*(tiledim-2)+y-1] = tile[x][y]

for fl in final:
    for c in fl:
        if c == '#':
            final_x += 1

m = open('monster.txt', 'r')
monster = []
monster_x = 0
for line in m.read().split('\n'):
    if len(line) > 0:
        lline = list(line)
        for c in lline:
            if c == '#':
                monster_x += 1
        monster.append(lline)

def has_monster(final, monster):
    count = 0
    for si in xrange(len(final) - len(monster)):
        for sj in xrange(len(final[0]) - len(monster[0])):
            matches = True
            for i in xrange(len(monster)):
                for j in xrange(len(monster[0])):
                    if monster[i][j] == '#' and final[si+i][sj+j] != '#':
                        matches = False
                        break
                if not matches:
                    break
            if matches:
                count += 1
    return count

for o in xrange(2):
    for r in xrange(4):
        fx = flip_tile(final, o ,r)
        matches = has_monster(fx, monster)
        if matches > 0:
            print final_x - monster_x * matches
            

