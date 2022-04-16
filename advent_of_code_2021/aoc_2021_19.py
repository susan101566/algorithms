import math
from collections import defaultdict

def difft(t1, t2):
    r = []
    for i in xrange(3):
        r.append(t2[i] - t1[i])
    return tuple(r)

'''
tsfms = [
    # y is up
    (1, 2, 3),
    (-3, 2, 1),
    (-1, 2, -3),
    (3, 2, -1),

    #  -y is up
    (-1, -2, 3),
    (-3, -2, -1),
    (1, -2, -3),
    (3, -2, 1),

    # x is up
    (-2, 1, 3),
    (-3, 1, -2),
    (2, 1, -3),
    (3, 1, 2),

    # -x is up
    (2, -1, 3),
    (-3, -1, 2),
    (-2, -1, -3),
    (3, -1, -2),

    # z is up
    (2, 3, 1),
    (-1, 3, 2),
    (-2, 3, -1),
    (1, 3, -2),

    # -z is up
    (1, -3, 2),
    (-2, -3, 1),
    (-1, -3, -2),
    (2, -3, -1),
]

sign = lambda x: math.copysign(1, x)
need_at_least = 12

# transform one point according to the ith transform
def transform_point(p, ti):
    t = tsfms[ti]
    nr = [0, 0, 0]
    for i in xrange(3):
        ti = t[i]
        tia = abs(ti)
        nr[tia - 1] = p[i] * sign(ti)
    return tuple(nr)

def sumt(t1, t2):
    r = []
    for i in xrange(3):
        r.append(t2[i] + t1[i])
    return tuple(r)

def addt(t1, diff):
    r = []
    for i in xrange(3):
        r.append(t1[i] + diff[i])
    return tuple(r)

def match(readings0, readings1):
    for i, r0 in enumerate(readings0):
        for j, r1 in enumerate(readings1):
            diff = difft(r0, r1)
            total = []
            for r3 in readings0:
                if addt(r3, diff) in readings1:
                    total += r3
            if len(total) >= need_at_least:
                return (diff, total)
    return None

# try to match 1 relative to 0.
def compare(sreading0, sreading1):
    for ti in xrange(len(tsfms)):
        points1 = []
        for reading in sreading1:
            points1.append(transform_point(reading, ti))
        match_result = match(sreading0, points1)
        if match_result != None:
            a, b = match_result
            return (a, b, ti)
    return None

f = open('input.txt', 'r')
readings = f.read().strip().split('\n\n')
scanner_readings = []
for reading in readings:
    sr = []
    for coordstr in reading.split('\n')[1:]:
        coord = map(int, coordstr.split(','))
        sr.append(coord)
    scanner_readings.append(sr)

# {0: [(1, (1,2,3))]}
rel_graph = defaultdict(list)
for sri1, sr1 in enumerate(scanner_readings):
    for sri2, sr2 in enumerate(scanner_readings):
        result = compare(sr1, sr2)
        if result :
            relative_origin, points_1, transformi = result
            rel_graph[sri1].append((sri2, relative_origin, transformi))

print 'found relative graph ---------------'
print rel_graph

# find all relative to 0
num_scanners = len(scanner_readings)
def get_scanner_origins():
    origins = [None] * num_scanners
    origins[0] = (0, (0, 0, 0), [])
    frontier = [0]
    while len(frontier) > 0:
        f = frontier.pop(-1)
        fi, fo, frs = origins[f]
        neis = rel_graph[fi]
        for (ni, no, ori) in neis:
            nv = no
            for fr in frs[::-1]:
               nv = transform_point(nv, fr)
            nv = sumt(fo, nv)
            if origins[ni] != None and nv != origins[ni][1]:
                print 'clashing', ni, ':', nv, origins[ni][1]
            if origins[ni] != None:
                continue
            transform_chain = frs[:]
            transform_chain.append(ori)
            origins[ni] = (ni, nv, transform_chain)
            frontier.append(ni)
    return origins

origins = get_scanner_origins()
print 'found origins----------------'
print origins
beacons = set()
for si, readings in enumerate(scanner_readings):
    _, origin, frs = origins[si]
    for r in readings:
        nv = r
        for fr in frs[::-1]:
            nv = transform_point(nv, fr)
        nv = difft(origin, nv)
        beacons.add(nv)
print len(beacons)
'''
# part 2
origins = [(0, (0, 0, 0), []), (1, (-1242.0, 114.0, -1281.0), [5]), (2, (-1260.0, -1127.0, -130.0), [22]), (3, (-77.0, 115.0, -1203.0), [14]), (4, (-1312.0, 1365.0, 2268.0), [7, 5, 18]), (5, (-2541.0, -1211.0, -1223.0), [11, 0, 19]), (6, (1037.0, 79.0, -1249.0), [17]), (7, (-15.0, -1071.0, -2503.0), [11, 0, 21]), (8, (-134.0, 2389.0, -1296.0), [11, 0, 16, 23, 10, 14, 1]), (9, (-49.0, 1358.0, 2423.0), [7, 22]), (10, (-1.0, -3502.0, 27.0), [23, 23, 13]), (11, (-85.0, 1257.0, -2529.0), [11, 0, 16, 23, 10, 14]), (12, (16.0, 1.0, 2290.0), [7, 5]), (13, (-21.0, 1353.0, -1367.0), [20]), (14, (-150.0, 54.0, 1133.0), [7]), (15, (-168.0, -2290.0, -96.0), [23, 23]), (16, (-1311.0, -2340.0, -2468.0), [11, 0, 23]), (17, (2.0, 58.0, -3593.0), [11, 0, 16, 23, 10]), (18, (-1225.0, 2488.0, -1310.0), [11, 0, 16, 23, 10, 14, 1, 11]), (19, (-72.0, 11.0, -2511.0), [11, 0, 16, 10]), (20, (-79.0, -3526.0, -1210.0), [23, 23, 5]), (21, (-135.0, -1083.0, -1298.0), [15]), (22, (-1286.0, -1210.0, -1317.0), [11, 0]), (23, (-1337.0, -1099.0, -3663.0), [11, 0, 16, 23]), (24, (-34.0, -1197.0, -115.0), [23]), (25, (1113.0, 98.0, -2425.0), [11, 0, 16, 23, 10, 12]), (26, (1160.0, 130.0, -3771.0), [11, 0, 16, 23, 10, 13]), (27, (2345.0, -4.0, -1359.0), [11, 0, 16, 23, 10, 12, 2]), (28, (-1203.0, 1191.0, 3577.0), [7, 5, 18, 8]), (29, (-1264.0, -1056.0, -2377.0), [11, 0, 16]), (30, (-1235.0, 8.0, -68.0), [11])]
maxi = 0
for _, v1, _ in origins:
    for _, v2, _ in origins:
        maxi = max(maxi, sum(map(abs, difft(v1, v2))))
print maxi
